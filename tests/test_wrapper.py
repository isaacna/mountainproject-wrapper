from wrapper import MP

def test_mp_info():
    mp_instance = MP('abc-123', 'johndoe@gmail.com')
    response = mp_instance.data()

    assert isinstance(response, dict)
    assert response['key'] == 'abc-123' and response['email']=='johndoe@gmail.com', "The ID should be in response"
