import sqlite3
from utils.db_api.sqlite import Database


def test():
    db = Database(path_to_db="test.db")
    try:
        db.create_table_hodimlar()
    except Exception as err:
        pass
    try:
        db.add_hodimlar(880082409, "direktor", "https://tatunf.uz/images/stories/people/kaipbergenov.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali direktori</b> \nKaipbergenov Batirbek Tulepbergenovich")
        db.add_hodimlar(1060795515, "direktor", "https://tatunf.uz/images/stories/people/rashid.jpg",
                    "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali Yoshlar masalalari va ma'naviy, ma'rifiy ishlar bo'yicha direktorning birinchi o'rinbosari</b>\nOteniyazov Rashid Idrisovich")
        db.add_hodimlar(5898566855, "direktor", "https://tatunf.uz/images/stories/people/seytkamalov_q.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali o’quv va tarbiyaviy ishlar bo’yicha direktor o’rinbosari</b> /nSeytkamalov Xayratdin Maulenovich")
        db.add_hodimlar(4, "dekan", "https://tatunf.uz/images/stories/people/tberdimbetov.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali \"Kompyuter injiniringi\" fakulteti dekani, PhD</b> \nBerdimbetov Timur Tileubergenovich")
        db.add_hodimlar(5, "dekan", "https://tatunf.uz/images/stories/people/bfayzullaev.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali \"Telekommunikatsiya texnologiyalari va kasbiy ta'lim\" fakulteti dekani, PhD</b> \nFayzullaev Bayram Artikbaevich")
        db.add_hodimlar(6, "dekan", "https://tatunf.uz/images/stories/maxambetov%20polat00.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali \"Kompyuter injiniringi\" fakulteti o'quv ishlari bo'yicha dekani o'rinbosari</b>\nMaxambetov Polat Jalgasbaevich")
        db.add_hodimlar(7, "kafedra", "https://tatunf.uz/images/stories/people/utewliev.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali \"Dasturiy injiniring\" kafedrasi mudiri, fizika-matematika fanlari doktori, professor</b>\nUtewliev Nietbay Utewlievich")
        db.add_hodimlar(8, "kafedra", "https://tatunf.uz/images/stories/people/tureniyazova.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali \"Axborot texnologiyalari\" kafedrasi mudiri, f.-m.f.n</b>\nTureniyazova Asiya Ibragimovna")
        db.add_hodimlar(9, "kafedra", "https://tatunf.uz/images/stories/people/gabilova.jpg", "<b>Toshkent axborot texnologiyalari universiteti Nukus filiali \"Kompyuter tizimlari\" kafedrasi mudiri, PhD</b>\nAbilova Gulbaxar Jalgasbayevna")

        db.add_hodimlar(139626906, "bo'limlar", "https://tatunf.uz/images/stories/people/sherzod.jpg", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali O'quv-metodik bo'limi boshlig'i</b>\nYadgarov Sherzod Abdullaevich")
        db.add_hodimlar(242876486, "boshqa", "https://scholar.googleusercontent.com/citations?view_op=view_photo&user=pzcwr68AAAAJ&citpid=1", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali PhD (t.f.f.d.) hodimi</b>\nM.A.Artikbayev")

        db.add_hodimlar(11, "bo'limlar", "https://tatunf.uz/images/stories/people/bnurimbetov.jpg", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Yoshalr bilan ishlash, ma'naviyat va ma'rifat bo'limi boshlig'i</b>\nNurimbetov Baxbergen Tolibaevich")
        db.add_hodimlar(12, "bo'limlar", "https://tatunf.uz/images/stories/people/allanazarovaral.jpeg", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Iqtidorli talabalarning ilmiy-tadqiqot ishlarini tashkil etish bo'limi boshlig'i</b>\nAllanazarov Aral Bisenbayevich")
        db.add_hodimlar(13, "markaz", "https://tatunf.uz/images/stories/people/xamdam.jpg", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Raqamli ta`lim texnologiyalari markazi boshlig'i</b>\nKenjaev Xamdam Bazarbaevich")
        db.add_hodimlar(14, "markaz", "https://tatunf.uz/images/stories/people/jyusupova.jpg", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Axborot resurs markazi boshlig'i</b>\nYusupova Jamila Karamatdinovna")
        db.add_hodimlar(15, "markaz", "https://tatunf.uz/images/stories/people/apirniyazov.jpg", "<b>Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Nukus filiali Jismoniy va yuridik shaxslarni murojatlari bila ishlash, nazorat va monitoring bo'limi boshlig'i</b>\nPirniytazov Ajiniyaz Kuniyazovich")

    except sqlite3.IntegrityError as err:
        pass

    hodimlar = db.select_all_hodimlar()
    print(f"Barcha fodyalanuvchilar: {hodimlar}")

    hodim = db.select_hodimlar(kalit="bo'limlar")

    print(f"Bitta foydalanuvchini ko'rish: {hodim}")
    #
    # hodim = db.select_kalit(kalit="mar*")
    #
    # print(f"ZZZZZZZZZZZZ: {hodim}")

test()
