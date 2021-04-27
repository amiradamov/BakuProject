import pickle
from config import ROOT_DIR

from nltk import word_tokenize

from aznlp.azerbaijani_lemmatizer import AzerbaijaniLemmatizer
from aznlp import word_noise_remover
from aznlp import stopword_remover
from text_classification.sentence_cleaner import *
from nltk.tokenize import word_tokenize


class NBC:
    
    def __init__(self):
        self.training_data_file = open(ROOT_DIR + '/text_classification/pickles/trainingdata_NB.pickle', 'rb')
        self.classifier = pickle.load(self.training_data_file, encoding='utf-8')

#     custom_sentence = """ 1750-ci ildə Qarabağ xanlığı yaradılır. 14 may 1805-ci ildə Qarabağ xanlığı Rusiya dövlətinin himayəsini qəbul edir. 1823-cü ildə ilk rəsmi siyahıyaalmaya görə, Dağlıq Qarabağ ərazisində yaşayan 18563 ailədən yalnız 1559-u və ya 8,4%-i erməni ailələridir. 1827-ci ildə Qafqaz Arxeoqrafiq Komissiyasının aktına əsasən Qarabağın Dağlıq hissəsində 12 min ailə yaşayırdı ki, bunlardan da yalnız 2,5 mini qeyri-müsəlmanlar idi. 1828-1830-cu illərdə Türkmənçay müqaviləsinə əsasən İrandan 40 min, Türkiyədən 84 min nəfər erməni köçürülərək, İrəvan və Yelizavetpol (indiki Gəncə) qəzalarında yerləşdirilir. Gəncə qəzasına göndərilənlərin çoxu indiki Ağdərə rayonu ərazisinə yerləşdirilir. 1832-ci ildə Dağlıq Qarabağ ərazisində köçürmələr nəticəsində ermənilərin sayı 34,8%-ə çatdırılır. 1886-cı ildə "Qafqaz təqvimi" məcmuəsində göstərilir ki, Zəngəzur mahalında azərbaycanlılar 45,7%, ermənilər 24,8%, digər millətlər isə 29,5% təşkil edir.

# 1905-ci ilin fevral ayında erməni terror təşkilatları Bakı, İrəvan, Zəngəzur, Qarabağ, Naxçıvan və digər yerlərdə azərbaycanlılara qarşı kütləvi qırğınlara başlayırlar, 50 min nəfərdən artıq azərbaycanlı qətlə yetirilir. 1905-ci ildə erməni dəstələri Şuşanın azərbaycanlılar yaşayan məhəllərinə hücuma keçirlər, 100-ə qədər azərbaycanlı ödürülür, 20-ə qədər ev yandırılır. 1905-ci il dekabrda Əhməd bəy Ağaoğlunun başçılığı altında "Difai" (Müdafiə) təşkilatı yaradılır. 1905-ci il 26 dekabrda Ağdərə rayonunun 500 nəfərlik Umudlu kənd sakinləri Ağdama pənah apararkən yolda Avram Hampanın dəstəsi tərəfindən qətlə yetirilirlər. 1906-cı ilin iyul ayında erməni silahlıları ikinci dəfə Şuşaya hücum edirlər.

# 1918-ci ildə İrəvan quberniyasının 4 mahalında 199 Azərbaycan kəndi dağıdılır, 135 min nəfər azərbaycanlı didərgin salınır. 1918-ci il 17 martda Urmiya şəhərində erməni terrorçuları 10 min nəfərdən artıq azərbaycanlını qətlə yetirirlər. Həmin tarixdən başlayaraq bir ay ərzində Urmiya, Salmas, Xoy, Maku, Şərəfxan və digər yerlərdə 100 mindən artıq adam öldürülür. 1918-ci il 18 martda Şamaxı qəzasının 53 kəndində ermənilər 8 min 27 nəfəri, o cümlədən 4190 kişi, 2560 qadın, 1277 uşağı qətlə yetirmişlər. Həmin ayın sonuna qədər öldürülənlərin sayı 12 min nəfərə çatdırılır. 1918-ci il mart ayından aprelə kimi Bakı şəhərində ermənilər tərəfindən 18 min azərbaycanlı qətlə yetirilir və bu hadisələr tarixdə Mart soyqırımı kimi qalır. 1918-ci il 1-9 mayda Quba qəzasında 122 kənd dağıdılır, 2800 nəfər azərbaycanlı öldürülür. 1918-ci il 29 mayda Azərbaycan parlamenti (Milli Şura) Antanta dövlətlərinin davamlı təzyiqlərindən sonra Azərbaycan şəhəri İrəvanın Ermənistana verilməsi haqda qərar qəbul edir. 1918-ci ilin yay və payız aylarında Zəngəzur qəzasında 115 azərbaycanlı kəndi ermənilər tərəfindən dağıdılır, 7729 azərbaycanlı öldürülür.

# 1919-cu il 29 yanvarda Qarabağ general-qubernatorluğu yaradılır.
#   1920-ci il dekabrın 1-də Azərbaycanın Zəngəzur mahalının böyük hissəsi Moskva rəhbərliyinin qərarı ilə Ermənistana verilir. 1923-cü il 7 iyulda Moskva rəhbərliyinin qərarı ilə Dağlıq Qarabağa [[Dağlıq Qarabağ Muxtar Vilayəti|muxtar vilayətstatusu verilir. 1923-cü il 18 sentyabrda Xankəndinin adı "Stepanakert" adlandırılır. 1929-cu il 18 fevralda Moskva rəhbərliyinin qərarı ilə [[Naxçıvan Muxtar Respublikası]]na məxsus olan 657 kv.km ərazi — Qurdbulaq, Horadiz, Oğbun, Almalı, İtqıran, Sultanbəy, Qarsevən, Kilid və digər kəndlər, həmçinin Zəngilan rayonunun Nüvədi kəndi, Qazax rayonunun 4400 hektarlıq meşə sahəsi Ermənistana verilir.

# 1930-cu ildə Moskva rəhbərliyinin qərarı ilə Naxçıvanın Əldərə, Lehvaz, Astazur və digər yaşayış məntəqələri Ermənistana verilir və bu ərazilər üzrə Mehri rayonu yaradılır. 1938-ci ildə Moskva rəhbərliyinin qərarı ilə Naxçıvanın Sədərək və Kərki kəndlərinin bir hissəsi Ermənistana verilir.

# 28 noyabr 1945-ci ildə Ermənistan rəhbəri Harri Arutinov Stalinə müraciət edərək Dağlıq Qarabağın Ermənistana birləşdirilməsini xahiş edir. 1947-1953-cü illərdə Ermənistanda toplum şəkildə yaşayan 150 min nəfərdən artıq azərbaycanlı SSRİ rəhbərliyinin qərarı ilə Azərbaycana köçürülür.

# 1965-ci ildə Xankəndində yaşayan M.Hovenesyan 13 nəfər erməninin imzası ilə Dağlıq Qarabağın Ermənistana birləşdirilməsi xahişi ilə məktubu SSRİ Ali Sovetinə göndərir. 1967-ci ilin iyun-avqust aylarında Dağlıq Qarabağın Xocavənd rayonunun Kuropatkin kəndində erməni Benikin uşağı yoxa çıxır, sonra isə onun meyidi Ələmşah Mustafayevin briqadasına məxsus olan sahədən tapılır. Bu hadisəyə görə briqadir Ələmşah, direktor Ərşad, kənd sakini Zöhrab həbs olunurlar. Bu şəxslərin günahı sübut olunmadığına görə məhkəmə işi yenidən istintaqa qaytarılır. Lakin ermənilər yolda həbsxana maşınını saxladır, onu çevirir, hər üç nəfəri öldürür, sonra da yandırırlar. Az sonra sübut olunur ki, uşağı öz dayısı öldürüb.

# 1969-cu ildə Xankəndidə "Qarabağ" mehmanxanasının eyvanından qumbara atılır, üç azərbaycanlı yaralanır. 1969-cu ildə Laçın rayonunun Qaragöl ərazisinin, Qubadlı rayonunun Çayzəmi ərazilərinin, Qazax rayonunun Kəmərli kənd ərazilərinin, Kəlbəcər rayonunun Zod qızıl yatağı ərazilərinin bir hissəsi Moskva rəhbərliyinin qərarı ilə Ermənistana verilir.

# 1982-ci ildə Moskva rəhbərliyinin qərarı ilə Qazax rayonunun İncədərə yaylağı, Kəmərli, Aslanbəyli, Qayınaqlı kəndləri ərazilərinin bir hissəsi Ermənistana verilir. 1985-ci ilin dekabr ayında Daşnaksütyun partiyasının Afinada keçirilən XXII qurultayı "Böyük Ermənistan" uğrunda mübarizəni genişləndirmək qərarını qəbul edir. 1986-cı ildə Moskva rəhbərliyinin qərarı ilə Qazax rayonunun 2500 hektarlıq ərazisi Ermənistana verilir.

# 1987-ci ildə akademik Abel Aqambekyanın təkidi ilə Parisdə keçirilən erməni ümummilli konqresi SSRİ-də yaranmaqda olan dəyişiklikərdən istifadə edərək Dağlıq Qarabağın Ermənistana birləşdirilməsi barədə qərar qəbul edir. 1987-ci il iyun-iyul aylarında rmənilər Xankəndinin küçələrində vərəqələr yayır, Dağlıq Qarabağın Azərbaycandan ayrılması üçün təbliğata başlayırlar. 1987-ci il oktyabr ayında İrəvanda "Qarabağ komitəsi" ilk açıq mitinq keçirir. Komitəyə İqor Muradyan və Levon Ter-Petrosyan başçılıq edirlər. 1987-ci il noyabrın 16-də Mixail Qorbaçovun iqtisadi məsələlər üzrə müşaviri Abel Aqambekyan Parisdə qəzetlərə müsahibə verərək, Dağlıq Qarabağın Ermənistana verilməsi ilə əlaqədar Qorbaçovu razı saldığını bildirir. """

#     custom_sentence = """1920-ci il dekabrın 1-də Azərbaycanın Zəngəzur mahalının
#     böyük hissəsi Moskva rəhbərliyinin qərarı ilə Ermənistana
#     verilir. 1923-cü il 7 iyulda Moskva rəhbərliyinin qərarı ilə
#     Dağlıq Qarabağa [[Dağlıq Qarabağ Muxtar Vilayəti|muxtar
#     vilayətstatusu verilir. 1923-cü il 18 sentyabrda Xankəndinin
#     adı Stepanakert adlandırılır. 1929-cu il 18 fevralda Moskva
#     rəhbərliyinin qərarı ilə [[Naxçıvan Muxtar Respublikası]]na
#     məxsus olan 657 kv.km ərazi — Qurdbulaq, Horadiz, Oğbun, Almalı,
#     İtqıran, Sultanbəy, Qarsevən, Kilid və digər kəndlər, həmçinin
#     Zəngilan rayonunun Nüvədi kəndi, Qazax rayonunun 4400 hektarlıq
#     meşə sahəsi Ermənistana verilir.

#     1930-cu ildə Moskva rəhbərliyinin qərarı ilə Naxçıvanın
#     Əldərə, Lehvaz, Astazur və digər yaşayış məntəqələri
#     Ermənistana verilir və bu ərazilər üzrə Mehri rayonu
#     yaradılır. 1938-ci ildə Moskva rəhbərliyinin qərarı ilə
#     Naxçıvanın Sədərək və Kərki kəndlərinin bir hissəsi
#     Ermənistana verilir.

#     28 noyabr 1945-ci ildə Ermənistan rəhbəri Harri Arutinov Stalinə
#     müraciət edərək Dağlıq Qarabağın Ermənistana birləşdirilməsini
#     xahiş edir. 1947-1953-cü illərdə Ermənistanda toplum şəkildə
#     yaşayan 150 min nəfərdən artıq azərbaycanlı SSRİ rəhbərliyinin
#     qərarı ilə Azərbaycana köçürülür.

#     1965-ci ildə Xankəndində yaşayan M.Hovenesyan 13 nəfər erməninin
#     imzası ilə Dağlıq Qarabağın Ermənistana birləşdirilməsi
#     xahişi ilə məktubu SSRİ Ali Sovetinə göndərir. 1967-ci ilin
#     iyun-avqust aylarında Dağlıq Qarabağın Xocavənd rayonunun Kuropatkin
#     kəndində erməni Benikin uşağı yoxa çıxır, sonra isə onun meyidi
#     Ələmşah Mustafayevin briqadasına məxsus olan sahədən tapılır. Bu
#     hadisəyə görə briqadir Ələmşah, direktor Ərşad, kənd sakini
#     Zöhrab həbs olunurlar. Bu şəxslərin günahı sübut olunmadığına
#     görə məhkəmə işi yenidən istintaqa qaytarılır. Lakin ermənilər
#     yolda həbsxana maşınını saxladır, onu çevirir, hər üç nəfəri
#     öldürür, sonra da yandırırlar. Az sonra sübut olunur ki, uşağı
#     öz dayısı öldürüb.

#     1969-cu ildə Xankəndidə "Qarabağ" mehmanxanasının eyvanından
#     qumbara atılır, üç azərbaycanlı yaralanır. 1969-cu ildə
#     Laçın rayonunun Qaragöl ərazisinin, Qubadlı rayonunun Çayzəmi
#     ərazilərinin, Qazax rayonunun Kəmərli kənd ərazilərinin,
#     Kəlbəcər rayonunun Zod qızıl yatağı ərazilərinin bir hissəsi
#     Moskva rəhbərliyinin qərarı ilə Ermənistana verilir.

#     1982-ci ildə Moskva rəhbərliyinin qərarı ilə Qazax rayonunun
#     İncədərə yaylağı, Kəmərli, Aslanbəyli, Qayınaqlı kəndləri
#     ərazilərinin bir hissəsi Ermənistana verilir. 1985-ci ilin dekabr
#     ayında Daşnaksütyun partiyasının Afinada keçirilən XXII qurultayı
#     "Böyük Ermənistan" uğrunda mübarizəni genişləndirmək qərarını
#     qəbul edir. 1986-cı ildə Moskva rəhbərliyinin qərarı ilə Qazax
#     rayonunun 2500 hektarlıq ərazisi Ermənistana verilir.

#     1987-ci ildə akademik Abel Aqambekyanın təkidi ilə Parisdə
#     keçirilən erməni ümummilli konqresi SSRİ-də yaranmaqda olan
#     dəyişiklikərdən istifadə edərək Dağlıq Qarabağın Ermənistana
#     birləşdirilməsi barədə qərar qəbul edir. 1987-ci il iyun-iyul
#     aylarında rmənilər Xankəndinin küçələrində vərəqələr
#     yayır, Dağlıq Qarabağın Azərbaycandan ayrılması üçün
#     təbliğata başlayırlar. 1987-ci il oktyabr ayında İrəvanda
#     "Qarabağ komitəsi" ilk açıq mitinq keçirir. Komitəyə İqor
#     Muradyan və Levon Ter-Petrosyan başçılıq edirlər. 1987-ci il
#     noyabrın 16-də Mixail Qorbaçovun iqtisadi məsələlər üzrə
#     müşaviri Abel Aqambekyan Parisdə qəzetlərə müsahibə verərək,
#     Dağlıq Qarabağın Ermənistana verilməsi ilə əlaqədar Qorbaçovu
#     razı saldığını bildirir."""

#     custom_sentence = """ Aləmlərin Rəbbi (sahibi) olan Allaha həmd olsun. O, Rəhman və Rəhimdir (mərhəmətlidir).
#     Din (qiyamət) gününün sahibidir. Ancaq sənə qulluq edir, yalnız Səndən kömək istəyirik. Bizi doğru yola hidayət
#     et. Nemət verdiyin kəslərin yoluna. Qəzəbinə düçar olanların və zəlalətdə olanların yoluna deyil. Qul huvallahu
#     Əhəd. Allahus-Saməd. Ləm yəlid və ləm yuləd. Və ləm yəkulləhu kufuvən Əhəd. De ki: O Allah təkdir. Allah
#     ehtiyacsızdır. Doğmamış və doğulmamışdır. Heç kəs də Onun bənzəri olmamışdır. Əsrə (əsr vaxtına) and olsun ki,
#     İnsan ziyan içindədir. Ancaq inanıb yaxşı əməl edən, bir-birinə haqqı və səbri tövsiyə edənlər ziyana
#     uğramazlar. Mən qaranlığı yarıb səhəri çıxaran Rəbbə sığınıram. Yaratdığı şeylərin şərrindən, qaranlıq çökdüyü
#     zaman gecənin şərrindən, düyünlərə üfləyən qadınların şərrindən, həsəd etdiyi zaman həsəd edənin şərrindən. Mən
#     insanların Rəbbinə sığınıram. İnsanların Sultanına, insanların Tanrısına. Vəsvəsə gətirib yoxa çıxan şeytanın
#     şərrindən. Hansı ki, insanların ürəyini vəsvəsə ilə doldurur. Cinlərin və insanların şərrindən. O Allah təkdir.
#     Allah ehtiyacsızdır. Doğmamış və doğulmamışdır. Heç kəs də Onun bənzəri olmamışdır. Allahım! Sən pis
#     sifətlərdən təmiz və uzaqsan. Səni həmişə belə uca tuturam (mədh edirəm). Sənin adın mübarəkdir. Varlığın hər
#     şeydən üstündür. Səndən başqa tanrı yoxdur. Dil, bədən və mal ilə edilən bütün ibadətlər Allah üçündür. Ey
#     Peyğəmbər! Allahın salamı, rəhmət və bərəkətləri sənin üzərinə olsun. Salam, bizim və Allahın bütün yaxşı
#     qullarının üzərinə olsun. Şahidlik edirəm ki, Allahdan başqa Tanrı yoxdur və Məhəmməd onun qulu və elçi­sidir.
#     Allahım! Məhəmmədə və Məhəmməd ümmətinə xeyir və bərəkət ver. İbrahimə və İbrahimin ümmətinə verdiyin kimi.
#     Şübhəsiz tərifə layiq yalnız sənsən. Allahım! Səndən kömək, günahlarımızın bağışlanmasını və razı olduğun
#     şeylərə hidayət etməni istəyirik. Sənə inanırıq və Sənə tövbə edirik və Sənə təvəkkül edirik. Bizə verdiyin
#     bütün nemətləri dərk edərək Səni xeyir ilə mədh edirik. Sənə şükr edirik və verdiyin hər bir neməti qəbul və
#     təsdiq edirik. Həqiqətən, sən göndərilən peyğəmbərlərdənsən. Ataları xəbərdar edilmədiyinə görə qəflət içində
#     olan bir qövmü xəbərdar edəsən deyə nazil edilmişdir. Həqiqətən, onların əksəriyyəti barəsində söz (əzab hökmü)
#     vacib olmuşdur. Çünki onlar iman gətirməzlər. Biz onların boyunlarına çənələrinə dirənən zəncirlər vurduq. Buna
#     görə də başları yuxarı qalxmışdır. Sən yalnız Qurana tabe olan və görmədiyi halda Rəhman olan Allahdan qorxan
#     kimsəni xəbərdar edə bilərsən. Buna görə də onu bağışlanma və gözəl bir mükafatla müjdələ! O zaman Biz onlara
#     iki elçi göndərmişdik. Ancaq onlar ikisini də təkzib etmişdilər. Biz də onları üçüncü bir elçi ilə
#     dəstəkləmişdik. Onlar: “Həqiqətən, biz (Allah tərəfindən) sizə göndərilən elçilərik!” - dedilər. """

#     custom_sentence = """
# Hərbi nazir Ənvər paşanın komandan Xəlil paşaya göndərdiyi təbrik teleqramında Xəzər dənizi sahillərində yerləşmiş Türkiyə ordusu Bakıya daxil olunan sonra hücumlarını Xəzər dənizinin sahili boyunca davam etdirərək Dağıstana çatır. 
# İzzət paşanın komandanlığı tutmuş, həm də bu əməliyyat zamanı türk ordusu tərəfindən Biçeraxovun ordusuna yardım göstərməyə cəhd edən Xəzər hərbi donanmasının iki hərbi gəmisi atəşə tutulmuş və sahildən uzaqlaşdırılmışdı. 
# 8 noyabrda Türkiyə ordusu Port-Petrovskdan Biçeraxovun ordusunu sıxışdırıb çıxarmış və onun ordusu dənizlə İranın şimalında yerləşən ingilislərin yanına qaçmışdı. 
# Lakin birinci dünya müharibəsində məğlub tarixli Mudros müqaviləsinin şərtlərinə görə öz ordusunu tezliklə Qafqaz-Xəzər bölgəsindən, həmçinin Azərbaycandan da çıxarmalı olur. 
# Başda Şimali İrandakı ingilis ordularının komandanı general-mayor nəqliyyat gəmisində İngilis generalı Bakıya yola düşməzdən əvvəl bu dövrdə müttəfiq dövlətlərin Azərbaycan Respublikasına münasibətini qeyd olunmuşdur ki, " Bakı onun neft sənayesi ilə birgə işğal olunacaq, ancaq ölkənin qalan bütün əraziləri Azərbaycan hökumətinin və onun ordusunun nəzarəti altında olacaq " və " Azərbaycan Paris sülh konfransının millətlərin öz müqəddəratını təyin etmək prinsipləri üzrə müzakirəsindən çıxarılmayacaqdır ". 
# Bəyanatda həmçinin qeyd olunmuşdu ki, Bakıya ingilis orduları ilə birlikdə Biçeraxovun hissələri də daxil olacaq, silahlı ermənilər isə buraya buraxılmayacaq. 
# Bütövlükdə, Britaniyanın Azərbaycanı işğal etməsinə müttəfiqlik ekspedisiyası donu geydirilmişdi. 
# Belə bir faktı qeyd etmək kifayətdir ki, " Prezident Krüger " flaqman gəmisində dörd Britaniya, Rusiya, Fransa və ABŞ bayraqları dalğalanırdı. 
# Doğrudur, burada ABŞ və Fransa orduları yox idi, ilk birinci iki dövlətin yalnız nümayəndələri var idi. 
# Tomson özünün ilk bəyanatlarında birmənalı qeyd etmişdi ki, müttəfiq orduları " Rusiya torpaqlarında " dır və Qafqaza gəliblər ki, " Rusiyanın Qara dənizlə Xəzər dənizi arasında yerləşən bu torpaqlarından ümumi təhlükəni uzaqlaşdırsınlar ". 
# İngilis generalının müraciətində qeyd olunurdu: " Bu ərazi ilə əlaqədar olan bütün məsələlərin qəti qərarı, qarşıda gələn sülh konfransında qəbul ediləcəkdir ". 
# İngilislər öz ordularının Xəzər dənizi bölgəsində gücləndirilməsinə xüsusi diqqət yönəltmişdilər. 
# Təsadüfi deyil ki, Çerçillin Hərbi Nazir kimi ilk imza etdiyi imperiya qərargahının rəisi Henri Vilsona tələb edirdi ki, " hazırda Bakı-Batumi dəmir yol xəttini əldə saxlayan ingilis silahlı qüvvələrinin həqiqi rolu necədir, həmçinin Xəzər dənizi sahillərinə nəzarət edən ingilis hərbi-dəniz qüvvələrinin vəziyyəti necədir? 
# Onlar özlərinin iştirakı ilə general Denikinin ordularına hansı səviyyədə yardım göstərirlər? 
# " Artıq sorğusuna ilin yazında yalnız Bakıda ingilis hərbi ingilis əsgəri və zabiti olduğu halda, həmin ilin yayında ingilis ordusunun şəxsi heyətinin ümumi sayı 5 minə çatdırılmışdı. 
# Bakını tutmaqla Xəzər bölgəsində ingilislərin mövqeyi xeyli dərəcədə möhkəmlənmişdi. 
# Bakının neft məhsullarını və əsas sənaye obyektlərini, həmçinin Xəzər hərbi və ticarət neft müdiriyyətinə " tabe etdirərək, Xəzər dənizində özünün hərbi-dəniz donanmasını yaratmaq üçün təcili tədbirlər görməyə başlamışdı. 
# Lakin onlar ilk mərhələdə böyük çətinliklərlə üzləşməli oldular. 
# İş onda idi ki, bir sıra gəmilərin, xüsusilə " Ərdəhan " və " Kars " gəmilərinin əsasən ruslardan komplektləşdirilmiş komanda heyəti həm ingilislərə, həm də ağqvardiyaçılara düşmən kimi baxırdı. 
# ildə Xəzər dənizinin qərb sahillərindəki ağqvardiyaçı ordusunun komandanlığının əməliyyat məlumatında deyilirdi: " Ən böyük gəmilərdən " Ərdəhan " və " Kars " pis vəziyyətdədir ". 
# " Qara dəniz ordusu " nun baş komandanı general ser illərdə onun komandanlığı altında olan ordunun Qafqazda və Xəzər ətrafındakı əməliyyatları haqqında məruzəsində İngiltərə hökumətinin " London qəzet " inin əlavəsində çap edildiyi " Ərdəhan " və " Kars " gəmilərinin, həmçinin bir neçə yardımçı torpeda katerləri tərəfindən batırılma qorxusu ilə ləğv olunmuşdular. 
# Beləliklə, matrosların " Kars " və " Ərdəhan " gəmilərini qaçırmağa göstərdikləri hər iki cəhdi ingilislər zərərsizləşdirmiş, hətta Nargen adası rayonundan " Kars " gəmisinə atəş açılmışdır, lakin torpeda gəmidən yan keçmişdir. 
# İngilislər tərəfindən bir çox Bu faktı nəzərə alaraq, həmçinin Xəzər dənizində layiqli hərbi-dəniz qüvvələri yaratmaq zərurəti ilə əlaqədar, ingilislər Xəzər dənizinə dəmir yolu ilə torpeda aparatları ilə silahlanmış, həmçinin gəmilərin sahildəki atəş mövqeyini qırıcı kater göndərmişdir. 
# sonra ingilislər Çeçen adasında özlərinin hərbi-dəniz aviasiya bazasını təşkil etdi. 
# böyük hərbi-dəniz vahidinə İngilislər Bakı-Krasnovodsk-Ənzəli üçbucağı üzərində nəzarət yaratmaqla, bütövlükdə, Xəzər akvatoriyasında özlərinin bütün hərbi strateji üstünlükləri ilə bərabər tam hökmranlığını təmin etməyə ümid edirdilər. 
# İngilis donanmasının əsas tapşırığı onun komandanı kommodor Norris tərəfindən müəyyən edilmişdi. 
# O yazırdı: " Biz Xəzər dənizinin şimal hissəsində yerləşən bolşevik qüvvələrinin, yerli bolşevizm təzahürlərinin və dənizdən bolşeviklərin çıxmasının qarşısını alırıq ". 
# yarısında dəniz vasitəsilə Denikinin və Kolçakın ağqvardiyaçı ordularını güclü şəkildə silahlandırır, neft məhsulları ilə təmin edirdi. 
# Bundan başqa general Milnin məlumatına görə " Britaniya ordusunun iştirakı respublikalarının orduları arasında hərbi əməliyyatların qarşısının alınmasına xidmət edirdi ". 
# Azərbaycan Respublikasına münasibətdə hiss olunacaq dərəcədə böyük siyasi dəyişikliklər özünü göstərdi. 
# ilin 7 dekabrında bütün siyasi partiyaların və təşkilatların, milli azlıqda qalan xalqların nümayəndələrinin təmsil olunduğu dekabrdaF. 
# Xoyskinin başçılığı ilə yeni dekabrda general Tomson yeni müdafiə etdiyini, " Azərbaycan hüdudlarında yeganə qanuni yerli hakimiyyət olduğu " nu bildirdi. 
# Cənubi Qafqazdakı birləşmiş ordusunun baş komandanı general Milnin Azərbaycan hökumətini tanımağını bir daha təsdiq etmiş və bununla əlaqədar qeyd etmişdir ki, " Zaqafqaziya dövlətlərinin daxili işlərinə heç bir müdaxilə olmayacaqdır ". 
# Fevralın axırlarında " Qafqaz-Kaspi hökuməti " nin, Biçeraxovun orduları Bakıdan çıxarıldı, erməni ordularının qalıqları ləğv edildi, Bakıya buraxıldı.
#     """
    def test(self, custom_sentence):
        
        # custom_tokens = [clean_tokens(word) for word in custom_sentence.split()]
        words = [w for w in custom_sentence.split()]
        custom_tokens = clean_tokens(words)
        # print(custom_tokens)
        # custom_tokens = clean_tokens(words)
        # print(custom_tokens)
        a = self.classifier.classify(dict([token, True] for token in custom_tokens))
        self.training_data_file.close()
        print(a)
        return a
