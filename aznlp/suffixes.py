inflectional_dict = {
    'Cəm': ['lar', 'lər'],
    'Mənsubiyyət 1-ci şəxs (tək)': ['m', 'ım', 'im', 'um', 'üm'],
    'Mənsubiyyət 2-ci şəxs (tək)': ['n', 'ın', 'in', 'un', 'ün'],
    'Mənsubiyyət 3-cü şəxs': ['sı', 'si', 'su', 'sü'],
    'Mənsubiyyət 1-ci şəxs (cəm)': ['ımız', 'imiz', 'umuz', 'ümüz'],
    'Mənsubiyyət 2-ci şəxs (cəm)': ['ınız', 'iniz', 'unuz', 'ünüz'],
    '1-ci şəxs (tək)': ['am', 'əm', 'yam', 'yəm', 'm'],
    '2-ci şəxs (tək)': ['san', 'sən', 'n'],
    '3-cü şəxs (tək)': ['dır', 'dir', 'dur', 'dür'],
    '1-ci şəxs (cəm)': ['ıq', 'ik', 'uq', 'ük', 'yıq', 'yik', 'yuq', 'yük', 'k', 'q'],
    '2-ci şəxs (cəm)': ['sınız', 'siniz', 'sunuz', 'sünüz', 'nız', 'niz', 'nüz', 'nuz'],
    '3-cü şəxs (cəm)': ['dırlar', 'dirlər', 'durlar', 'dürlər', 'lar'],
    'Yiyəlik hal': ['ın', 'in', 'un', 'ün', 'nın', 'nin', 'nun', 'nün'],
    'Yönlük hal': ['a', 'ə', 'ya', 'yə'],
    'Təsirlik hal': ['ı', 'i', 'u', 'ü', 'nı', 'ni', 'nu', 'nü'],
    'Yerlik hal': ['da', 'də'],
    'Çıxışlıq hal': ['dan', 'dən'],
    'İlə hissəciyi': ['la', 'lə'],
    'Inkar': ['ma', 'mə'],
    'Şühudi keçmiş zaman': ['dı', 'di', 'du', 'dü'],
    'Nəqli keçmiş zaman': ['mış', 'miş', 'muş', 'müş', 'ıb', 'ib', 'ub', 'üb', 'yıb', 'yib', 'yub', 'yüb'],
    'İndiki zaman': ['ır', 'ir', 'ur', 'ür', 'yır', 'yir', 'yur', 'yür'],
    'Inkarda indiki zaman': ['mır', 'mir', 'mur', 'mür'],
    'Qəti gələcək zaman': ['acaq', 'əcək', 'yacaq', 'yəcək'],
    'Qeyri-qəti gələcək zaman': ['ar', 'ər', 'yar', 'yər', 'r'],
    'Inkarda qeyri-qəti gələcək zaman': ['mar', 'mər', 'maz', 'məz'],
    'Əmr şəkli 1-ci şəxs (tək)': ['ım', 'im', 'um', 'üm', 'yım', 'yim', 'yum', 'yüm'],
    'Əmr şəkli 3-cü şəxs (tək)': ['sın', 'sin', 'sun', 'sün'],
    'Əmr şəki 1-ci şəxs (cəm)': ['aq', 'ək', 'yaq', 'yək'],
    'Əmr şəkli 2-ci şəxs (cəm)': ['ın', 'in', 'un', 'ün', 'yın', 'yin', 'yun', 'yün'],
    'Əmr şəkli 3-cü şəxs (cəm)': ['sınlar', 'sinlər', 'sunlar', 'sünlər'],
    'Arzu şəkli': ['a', 'ə', 'ya', 'yə'],
    'Vacib şəkli': ['malı', 'məli'],
    'Lazım şəkli': ['ası', 'əsi', 'yası', 'yəsi'],
    'Şərt şəkli': ['sa', 'sə'],
    'Məsdər': ['maq', 'mək'],
    'Feli sifət': ['yan', 'yən', 'an', 'ən', 'dıq', 'dik', 'duq', 'dük', 'ası', 'əsi', 'yası', 'yəsi', 'malı', 'məli'],
    'Feli bağlama': ['araq', 'ərək', 'yaraq', 'yərək', 'madan', 'mədən', 'malı', 'məli', 'anda', 'əndə', 'yandə', 'yəndə', 'dıqca', 'dikcə', 'duqca', 'dükcə', 'arkən', 'ərkən', 'yarkən', 'yərkən', 'ınca', 'incə', 'unca', 'üncə', 'yınca', 'yincə', 'yunca', 'yüncə'],
    'İdi hissəciyi': ['dı', 'di', 'du', 'dü'],
    'İmiş hissəciyi': ['mış', 'miş', 'muş', 'müş'],
    'İsə hissəciyi': ['sa', 'sə'],
    'İstisna leksik şəkilçilər': ['gil', 'dakı', 'dəki', 'kı', 'ki', 'ku', 'kü', 'sız', 'siz', 'suz', 'süz'],
    'Bitişdirici samitlər': ['y', 'n', 's']
}
inflectional = []

for k in inflectional_dict:
    for val in inflectional_dict[k]:
        inflectional.append(val)

inflectional.sort(key=len, reverse=True)
