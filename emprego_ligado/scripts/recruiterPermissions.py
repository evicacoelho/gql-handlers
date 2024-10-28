"""
Recruiter Permissions
Update a recruiter's permissions
"""

recruiterPermissions = """
mutation RecruiterPermissions($id: Int!, $role: String!, $permissions: [String!]!) {
    recruiterPermissions(
        id: $id,
        role: $role,
        permissions: $permissions
    ) {
        ... on Recruiter{
            activated
            branch
            branch_id
            company_id
            company_name
            created_at
            deleted_at
            email
            email_password_sent
            id
            mobile
            name
            phone
            rank
            role
            permissions
            updated_at
            user_id
        }
        ... on PermissionDenied{
            error
        }
        ... on RecordNotFound{
            error
        }
        ... on BadRequest{
            error
        }
    }
}
"""