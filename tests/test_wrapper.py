from wrapper import MP

def test_mp_info():
    mp_instance = MP('abc-123', 'johndoe@gmail.com')
    assert mp_instance.email == 'johndoe@gmail.com', "Email is incorrect" 
    assert mp_instance.key == 'abc-123', "Key is incorrect" 
