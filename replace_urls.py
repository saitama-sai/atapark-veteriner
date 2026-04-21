import os

def main():
    html_file = 'index.html'

    mapping = {
        'https://lh3.googleusercontent.com/aida/ADBb0ujHr1hJdIzmJBzt0gdGpZ5W7iHI0uFbzGbGqQO8-YKmV2TzVgg0nESZV2roqTPLVI06kg38EVig-nJyS7cKNXqMkAL8Rf0QU1iqGp139B6dpswP9gy4x3lZGrer_DkEHPVZWgtpVFY4r-Z-pznQ-R7-Fs4GPQaQGj_JiQYbLHIxxLWvCBXUK5DaGNrETdee1sFdtKgiWxeRDBlQ1U0ZNbbvugZeXIgFpMsM4QaVovqw4LMokr8a2mYz0w1IqprZcql9he9qnQNX': 'assets/images/vet_clinic_hero_1776796588451.png',
        'https://lh3.googleusercontent.com/aida/ADBb0ugj-_nO6NrIWxSGUL9KKWeFTMR9Ib4GrJ9cm2CRcqJUKhJ9hcRDH47bd2eKERnjqZwsqVlQuSAB2r1bPJ-3qQM3shpHcS_pH4gh0hMDLHjCNO3YBTB-BVkbVMNpbN4XEe-diVMzNcsBrV-xyAeLjaxMdiygF-TdHfmVXeEbYAjdMtF5XnfpyAl8xRx9wyVBS42DijTO4dkBKOFI3vBKl7fa-seN3pGgl-FKoXaabOdEyaz1kZZbPczSZW3bSCHYb64SDINPJH5M': 'assets/images/cute_cat_hero_1776796573273.png',
        'https://lh3.googleusercontent.com/aida/ADBb0ujGiLdDatE6ejmjc-dSmDu8ocBo7_r4I8h2_qfTRewhsZs5Z933sRrf2j0TExtnw6Yn4Oy_nLHm_MKlcBGxlVH0iZMTP_kaATlD-Oybi7b4plcTiYztCZ-OdJoH7EPZBR9DA4Xg4HbjIcL58Y40-TXzpJCvTBbHK2nm4g9s2BV9-Ev4sMGQAkg9GlPrlCgHM6C-d9E6twJF0ZTfwkpDrn2phU6uxwot6owjVL7bSBOV0af0Pb3nQQEn3kjFO5rNfFJc953m2VXoYg': 'assets/images/cute_dog_hero_1776796551196.png',
        'https://lh3.googleusercontent.com/aida/ADBb0ug4HGtRlR7Mg_6TAY-AvsC6GDuuCr__VL1c8VkUGEvOsVzkICT_n_sJGrjRYVv7dmTE_Q3MVaKNNc8Tb9XBZnVeGsWcZJhm2N4_UJPo1qN5mEcMBY8-uac255udbhrNIntCzf7eg7EzK_ty8B9iTXv5RidCsFnYnP_CHs7TPBC6HelNlHkt-Ia4ZxU-BwhPCXmM5XE1AmWv_2RXxtJpfvE_J1lDgErCcrfLBc7kAtD9LfUevW_8sscXPW7bphhXt70rYZvxXAhlxg': 'assets/images/pets_landscape_1776796632843.png',
        'https://lh3.googleusercontent.com/aida/ADBb0ugwHHGKAc06bfgshyfy56sVGUo0ruVTu992tVntOVarDFObO5lEKgWF86mJMdPqGOk2vYBglJWypgrPSU_49gJCV-0UYuzACz3bvs2Ck62y9INQ0SjG1hC5JoCHN9dgaRws-7ua9sqs9Yv-pw9fhVym0Cm7TWJfLwjgQJwuhCeNnWjvTL7XvBpEXSn57xqw6wTFYPT7cLXbcSAPf4TfltPB9miMeT_xX3LkYWamZlbreG84VSdOJdmg1Qrlr9sGN4ZZaoPPc6ci5Q': 'assets/images/cute_dog_display_1776796602538.png',
        'https://lh3.googleusercontent.com/aida/ADBb0uhOUCi_9k9PCUFbl_s_elzYs8KIoHlkwZL60Pvo1bcq77x3g-ygX6lY4VhLrjc-4iq04ijzd5ZHBdb_tzUYHFzlgXsKC-kniZ9FkiXExZ3UPcqxOjA8y3zNXnyBeYCBIcR1zP1e6R1VIvlNLSA1z0B6FeP7aj82evnYTSqGftqp-610tguzS_J886iOMWIiUhSzm6IAJHg0E0e_MHPaa2GK-lk_m3ufy3EDNZ6blOY0-qjJy7QNdTMfYdhXqM_4iXdbLI51-KTh': 'assets/images/cute_cat_display_1776796616105.png',
        'https://lh3.googleusercontent.com/aida/ADBb0ugToxE_Cw9FuQ_dQhAqrQSPOLPtpfO0AyLPvp3iDmMNsP3SU6wiwpgypGwY6S6vYPsVYslv7kHShIoaq-ncqMeqrTFpfh7qMpMDMhIwEB3Vhr4jqimG7QNzfuQlRXvoLdAYbxun2_xj9RJ7FWnLQ6IPLOHq-8uQTaxb3txcAZzDGEoNqKHcGOCK-InbVOT72LHSqC3autXTC9R5wqiXbRGvEcu3Swi9sjIRFl9fzsG9yXhPlvFDA3IsKBIzbFBRHU1F9wtEhJ1fhQ': 'assets/images/teddy_bear_about_1776796646846.png'
    }

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    for old_url, new_path in mapping.items():
        content = content.replace(old_url, new_path)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print("URLs successfully replaced!")

if __name__ == '__main__':
    main()
