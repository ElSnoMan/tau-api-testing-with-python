from bookstore import account_service as accounts


def test_create_authorized_user():
    CREDENTIALS = 'authorized_username', 'P@$$w0rd'

    user = accounts.create_user(*CREDENTIALS)
    token = accounts.generate_token(*CREDENTIALS)

    assert accounts.is_authorized(*CREDENTIALS) is True

    deletion = accounts.delete_user(user.userID, token.token)
    print('User deleted?', deletion.ok)
