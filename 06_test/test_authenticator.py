import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth

@pytest.mark.parametrize("username, password", [
    ("user1", "password1"),
    ("user2", "password2"),
    ("user3", "password3"),
])
def test_register(authenticator, username, password):
    authenticator.register(username, password)
    assert authenticator.users[username] == password

@pytest.mark.parametrize("username, password", [
    ("user1", "password1")
])
def test_register_fail(authenticator, username, password):
    authenticator.register(username, password)
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register(username, password)

@pytest.mark.parametrize("username, password", [
    ("user1", "password1")
])
def test_login(authenticator, username, password):
    authenticator.register(username, password)
    message = authenticator.login(username, password)
    assert message == "ログイン成功"

@pytest.mark.parametrize("username, password", [
    ("user1", "password1")
])
def test_login_fail(authenticator, username, password):
    authenticator.register(username, password)
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login(username, "password2")
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("user2", password)



