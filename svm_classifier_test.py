from text_classification.sentence_cleaner import *
import pickle

from config import ROOT_DIR


class SVMC:
    
    def __init__(self):
        self.vectorizer_file = open(ROOT_DIR + '/text_classification/pickles/trainingdata_vect_SVM.pickle', 'rb')
        self.SVM_file = open(ROOT_DIR + '/text_classification/pickles/trainingdata_model_SVM.pickle', 'rb')

        self.Tfidf_vect = pickle.load(self.vectorizer_file, encoding='utf-8')
        self.SVM = pickle.load(self.SVM_file, encoding='utf-8')

    # custom_sentence = input()

#     custom_sentence = """ Maddə 7. Azərbaycan dövləti
#
# I. Azərbaycan dövləti demokratik, hüquqi, dünyəvi, unitar respublikadır.
#
# II. Azərbaycan Respublikasında dövlət hakimiyyəti daxili məsələlərdə yalnız hüquqla xarici məsələlərdə isə yalnız Azərbaycan Respublikasının tərəfdar çıxdığı beynəlxalq müqavilələrdən irəli gələn müddəalarla məhdudlaşır.
#
# III. Azərbaycan Respublikasında dövlət hakimiyyəti hakimiyyətlərin bölünməsi prinsipi əsasında təşkil edilir:
#
# - qanunvericilik hakimiyyətini Azərbaycan Respublikasının Milli Məclisi həyata keçirir;
#
# - icra hakimiyyəti Azərbaycan Respublikasının Prezidentinə mənsubdur;
#
# - məhkəmə hakimiyyətini Azərbaycan Respublikasının məhkəmələri həyata keçirir.
#
# IV. Bu Konstitusiyanın müddəalarına əsasən qanunvericilik, icra və məhkəmə hakimiyyətləri qarşılıqlı fәaliyyәt göstərir və öz səlahiyyətləri çərçivəsində müstəqildirlər.
# Maddə 8. Azərbaycan dövlətinin başçısı
#
# I. Azərbaycan dövlətinin başçısı Azərbaycan Respublikasının Prezidentidir. O, ölkənin daxilində və xarici münasibətlərdə Azərbaycan dövlətini təmsil edir.
#
# II. Azərbaycan Respublikasının Prezidenti Azərbaycan xalqının vahidliyini təcəssüm etdirir və Azərbaycan dövlətçiliyinin varisliyini təmin edir.
#
# III. Azərbaycan Respublikasının Prezidenti Azərbaycan dövlətinin müstəqilliyinin, ərazi bütövlüyünün və Azərbaycan Respublikasının tərəfdar çıxdığı beynəlxalq müqavilələrə riayət olunmasının təminatçısıdır.
#
# IV. Azərbaycan Respublikasının Prezidenti məhkəmə hakimiyyətinin müstəqilliyinin təminatçısıdır.
# Maddə 9. Silahlı Qüvvələr
#
# I. Azərbaycan Respublikası öz təhlükəsizliyini və müdafiəsini təmin etmək məqsədi ilə Silahlı Qüvvələr yaradır. Silahlı Qüvvələr Azərbaycan Ordusundan və başqa silahlı birləşmələrdən ibarətdir.[1]
#
# II. Azərbaycan Respublikası başqa dövlətlərin müstəqilliyinə qəsd vasitəsi kimi və beynəlxalq münaqişələrin həlli üsulu kimi müharibəni rədd edir.
#
# III. Azərbaycan Respublikasının Prezidenti Azərbaycan Respublikası Silahlı Qüvvələrinin Ali baş komandanıdır.
# Maddə 10. Beynəlxalq münasibətlərin prinsipləri
#
# Azərbaycan Respublikası başqa dövlətlərlə münasibətlərini hamılıqla qəbul edilmiş beynəlxalq hüquq normalarında nəzərdə tutulan prinsiplər əsasında qurur.
# Maddə 11. Ərazi
#
# I. Azərbaycan Respublikasının ərazisi vahiddir, toxunulmazdır və bölünməzdir.
#
# II. Azərbaycan Respublikasının daxili suları, Xəzər dənizinin (gölünün) Azərbaycan Respublikasına mənsub olan bölməsi, Azərbaycan Respublikasının üzərindəki hava məkanı Azərbaycan Respublikası ərazisinin tərkib hissəsidir.
#
# III. Azərbaycan Respublikasının ərazisi özgəninkiləşdirilə bilməz. Azərbaycan Respublikası öz ərazisinin heç bir hissəsini heç bir şəkildə kimsəyə vermir; yalnız Azərbaycan Respublikası Milli Məclisinin qərarı ilə Azərbaycanın bütün əhalisi arasında referendum keçirmək yolu ilə Azərbaycan xalqının iradəsi əsasında dövlət sərhədləri dəyişdirilə bilər.
# Maddə 12. Dövlətin ali məqsədi
#
# I. İnsan və vətəndaş hüquqlarının və azadlıqlarının, Azərbaycan Respublikasının vətəndaşlarına layiqli həyat səviyyəsinin təmin edilməsi dövlətin ali məqsədidir.[2]
#
# II. Bu Konstitusiyada sadalanan insan və vətəndaş hüquqları və azadlıqları Azərbaycan Respublikasının tərəfdar çıxdığı beynəlxalq müqavilələrə uyğun tətbiq edilir.
# Maddə 13. Mülkiyyət
#
# I. Azərbaycan Respublikasında mülkiyyət toxunulmazdır və dövlət tərəfindən müdafiə olunur.
#
# II. Mülkiyyət dövlət mülkiyyəti, xüsusi mülkiyyət və bələdiyyə mülkiyyəti növündə ola bilər.
#
# III. Mülkiyyətdən insan və vətəndaş hüquqları və azadlıqları, cəmiyyətin və dövlətin mənafeləri, şəxsiyyətin ləyaqəti əleyhinə istifadə edilə bilməz.
# Maddə 14. Təbii ehtiyatlar
#
# Təbii ehtiyatlar hər hansı fiziki və ya hüquqi şəxslərin hüquqlarına və mənafelərinə xələl gətirmədən Azərbaycan Respublikasına mənsubdur.
# Maddə 15. İqtisadi inkişaf və dövlət
#
# I. Azərbaycan Respublikasında iqtisadiyyatın inkişafı müxtəlif mülkiyyət növlərinə əsaslanaraq xalqın rifahının yüksəldilməsinə xidmət edir.
#
# II. Azərbaycan dövləti bazar münasibətləri əsasında sosial yönümlü iqtisadiyyatın inkişafına şərait yaradır, azad sahibkarlığa təminat verir, iqtisadi münasibətlərdə inhisarçılığa və haqsız rəqabətə yol vermir.[3]
# Maddə 16. Sosial inkişaf və dövlət
#
# I. Azərbaycan dövləti xalqın və hər bir vətəndaşın rifahının yüksəldilməsi, onun sosial müdafiəsi və layiqli həyat səviyyəsi qayğısına qalır.
#
# II. Azərbaycan dövləti mədəniyyətin, təhsilin, səhiyyənin, elmin, incəsənətin inkişafına yardım göstərir, ölkənin təbiətini, xalqın tarixi, maddi və mənəvi irsini qoruyur.
# Maddə 17. Ailə, uşaqlar və dövlət[4]
#
# I. Cəmiyyətin əsas özəyi kimi ailə dövlətin xüsusi himayəsindədir.
#
# II. Uşaqların qayğısına qalmaq və onları tərbiyə etmək valideynlərin borcudur. Bu borcun yerinə yetirilməsinə dövlət nəzarət edir.
#
# III. Valideynləri və ya qəyyumları olmayan, valideyn qayğısından məhrum olan uşaqlar dövlətin himayəsindədirlər.
#
# IV. Uşaqları onların həyatına, sağlamlığına və ya mənəviyyatına təhlükə törədə bilən fəaliyyətə cəlb etmək qadağandır.
#
# V. 15 yaşına çatmamış uşaqlar işə götürülə bilməzlər.
#
# VI. Uşaq hüquqlarının həyata keçirilməsinə dövlət nəzarət edir.
# Maddə 18. Din və dövlət
#
# I. Azərbaycan Respublikasında din dövlətdən ayrıdır. Bütün dini etiqadlar qanun qarşısında bərabərdir.
#
# II. İnsan ləyaqətini alçaldan və ya insanpərvərlik prinsiplərinə zidd olan dinlərin (dini cərəyanların) yayılması və təbliği qadağandır.[5]
#
# III. Dövlət təhsil sistemi dünyəvi xarakter daşıyır.
# Maddə 19. Pul vahidi
#
# I. Azərbaycan Respublikasının pul vahidi manatdır.
#
# II. Pul nişanlarının tədavülə buraxılması və tədavüldən çıxarılması hüququ yalnız Mərkəzi Banka mənsubdur. Azərbaycan Respublikasının Mərkəzi Bankı dövlətin müstəsna mülkiyyətindədir.[6]
#
# III. Azərbaycan Respublikasının ərazisində manatdan başqa pul vahidlərinin ödəniş vasitəsi kimi işlədilməsi qadağandır.
# Maddə 20. Dövlətin borclarına qoyulan məhdudiyyətlər
#
# Azərbaycan dövlətinə qarşı qiyama və dövlət çevrilişinə kömək məqsədi ilə alınmış borclar Azərbaycan Respublikası tərəfindən öhdəlik kimi qəbul edilə və ödənilə bilməz.
# Maddə 21. Dövlət dili
#
# I. Azərbaycan Respublikasının dövlət dili Azərbaycan dilidir. Azərbaycan Respublikası Azərbaycan dilinin inkişafını təmin edir.
#
# II. Azərbaycan Respublikası əhalinin danışdığı başqa dillərin sərbəst işlədilməsini və inkişafını təmin edir.
# Maddə 22. Paytaxt
#
# Azərbaycan Respublikasının paytaxtı Bakı şəhəridir.
# Maddə 23. Azərbaycan dövlətinin rəmzləri
#
# I. Azərbaycan Respublikasının dövlət rəmzləri Azərbaycan Respublikasının Dövlət bayrağı, Azərbaycan Respublikasının Dövlət gerbi və Azərbaycan Respublikasının Dövlət himnidir.
#
# II. Azərbaycan Respublikasının Dövlət bayrağı bərabər enli üç üfüqi zolaqdan ibarətdir. Yuxarı zolaq mavi, orta zolaq qırmızı, aşağı zolaq yaşıl rəngdədir və qırmızı zolağın ortasında bayrağın hər iki üzündə ağ rəngli aypara ilə səkkizguşəli ulduz təsvir edilmişdir. Bayrağın eninin uzunluğuna nisbəti 1:2-dir.
#
# III. Azərbaycan Respublikası Dövlət bayrağının və Azərbaycan Respublikası Dövlət gerbinin təsviri, Azərbaycan Respublikası Dövlət himninin musiqisi və mətni Konstitusiya qanunu ilə müəyyən edilir.
#
#
# İkİncİ BÖLMƏ
# Əsas hüquqlar, azadlıqlar və vəzİfələr
#
# III fəsil
#
# Əsas İnsan və vətəndaş hüquqları və azadlıqları
# Maddə 24. İnsan və vətəndaş hüquqlarının və azadlıqlarının əsas prinsipi
#
# I. İnsan ləyaqəti qorunur və ona hörmət edilir.[7]
#
# II. Hər kəsin doğulduğu andan toxunulmaz, pozulmaz və ayrılmaz hüquqları və azadlıqları vardır.
#
# III. Hüquqlar və azadlıqlar hər kəsin cəmiyyət və başqa şəxslər qarşısında məsuliyyətini və vəzifələrini də əhatə edir. Hüquqlardan sui-istifadəyə yol verilmir.[8]
# Maddə 25. Bərabərlik hüququ[9]
#
# I. Hamı qanun və məhkəmə qarşısında bərabərdir.
#
# II. Kişi ilə qadının eyni hüquqları və azadlıqları vardır.
#
# III. Dövlət, irqindən, etnik mənsubiyyətindən, dinindən, dilindən, cinsindən, mənşəyindən, əmlak vəziyyətindən, qulluq mövqeyindən, əqidəsindən, siyasi partiyalara, həmkarlar ittifaqlarına və digər ictimai birliklərə mənsubiyyətindən asılı olmayaraq, hər kəsin hüquq və azadlıqlarının bərabərliyinə təminat verir. İnsan və vətəndaş hüquqlarını və azadlıqlarını irqi, etnik, dini, dil, cinsi, mənşəyi, əqidə, siyasi və sosial mənsubiyyətə görə məhdudlaşdırmaq qadağandır.[10]
#
# IV. Heç kəsə bu maddənin III hissəsində göstərilən əsaslara görə zərər vurula bilməz, güzəştlər və ya imtiyazlar verilə bilməz, yaxud güzəştlərin və ya imtiyazların verilməsindən imtina oluna bilməz.
#
# V. Hüquq və vəzifələrlə bağlı qərarlar qəbul edən dövlət orqanları və dövlət hakimiyyəti səlahiyyətlərinin daşıyıcıları ilə münasibətlərdə hər kəsin bərabər hüquqları təmin edilir.
#
# VI. Sağlamlıq imkanları məhdud olanlar, onların məhdud imkanlarına görə həyata keçirilməsi çətinləşən hüquq və vəzifələrdən başqa, bu Konstitusiyada təsbit olunmuş bütün hüquqlardan istifadə edir və vəzifələri daşıyırlar.[11]
# Maddə 26. İnsan və vətəndaş hüquqlarının və azadlıqlarının müdafiəsi
#
# I. Hər kəsin qanunla qadağan olunmayan üsul və vasitələrlə öz hüquqlarını və azadlıqlarını müdafiə etmək hüququ vardır.
#
# II. Dövlət hər kəsin hüquqlarının və azadlıqlarının müdafiəsinə təminat verir.
# Maddə 27. Yaşamaq hüququ
#
# I. Hər kəsin yaşamaq hüququ vardır.
#
# II. Dövlətə silahlı basqın zamanı düşmən əsgərlərinin öldürülməsi, məhkəmənin qanuni qüvvəyə minmiş hökmünə əsasən ölüm cəzasının tətbiqi və qanunla nəzərdə tutulmuş digər hallar istisna olmaqla, hər bir şəxsin yaşamaq hüququ toxunulmazdır.
#
# III. Müstəsna cəza tədbiri kimi ölüm cəzası, tam ləğv edilənədək , yalnız dövlətə, insan həyatına və sağlamlığına qarşı xüsusilə ağır cinayətlərə görə qanunla müəyyən edilə bilər.
#
# IV. Qanunla nəzərdə tutulmuş zəruri müdafiə, son zərurət, cinayətkarın yaxalanması və tutulması, həbsdə olanın həbs yerindən qaçmasının qarşısının alınması, dövlətə qarşı qiyamın yatırılması və ya dövlət çevrilişinin qarşısının alınması, ölkəyə silahlı basqın edilməsi halları istisna olmaqla insana qarşı silah işlədilməsinə yol verilmir."""

    def test(self, custom_sentence):
        

        words = [w for w in custom_sentence.split()]
        custom_tokens = clean_tokens(words)
        print(custom_tokens)
        custom_sentence = ' '.join(custom_tokens)
        print('-----------')
        vect = self.Tfidf_vect.transform([custom_sentence])
        print(vect)
        prediction = self.SVM.predict(vect)
        print(prediction)

        if prediction == 0:
            return 'Arxitektura'
        elif prediction == 1:
            return 'Din'
        elif prediction == 2:
            return 'Edebiyyat'
        elif prediction == 3:
            return 'Ekologiya'
        elif prediction == 4:
            return 'Elm'
        elif prediction == 5:
            return 'Felsefe'
        elif prediction == 6:
            return 'Herb'
        elif prediction == 7:
            return 'Huquq'
        elif prediction == 8:
            return 'Idman'
        elif prediction == 9:
            return 'Incesenet'
        elif prediction == 10:
            return 'Jurnalistika'
        elif prediction == 11:
            return 'Kend Teserrufati'
        elif prediction == 12:
            return 'Maliyye'
        elif prediction == 13:
            return 'Medeniyyet'
        elif prediction == 14:
            return 'Proqramlashdirma'
        elif prediction == 15:
            return 'Psixologiya'
        elif prediction == 16:
            return 'Rabite'
        elif prediction == 17:
            return 'Siyaset'
        elif prediction == 18:
            return 'Sosiologiya'
        elif prediction == 19:
            return 'Tarix'
        elif prediction == 20:
            return 'Tibb'
        elif prediction == 21:
            return 'Turizm'


        self.vectorizer_file.close()
        self.SVM_file.close()
