from translator import translate

def test_translate_halo():
    assert translate("halo") == "hello"

def test_translate_terima_kasih():
    assert translate("terima kasih") == "thank you"

def test_translate_tidak_ada():
    assert translate("rumah") == "kata tidak ditemukan"