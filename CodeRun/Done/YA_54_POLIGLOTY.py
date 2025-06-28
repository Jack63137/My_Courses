set_lang = []
all_langs = []
n_shkolnik = int(input())

for i in range(0,n_shkolnik):
    n_lang = int(input())
    langs =[]
    for i in range(0,n_lang):
        l = input()
        langs.append(l)
        set_lang.append(l)
    all_langs.append(langs)

set_forall_lang = all_langs[0]
for i in range(0,len(all_langs)-1):
    set_forall_lang = set(all_langs[i]) & set(all_langs[i+1]) & set(set_forall_lang)

set_forall_lang = set(set_forall_lang)
set_lang = set(set_lang)
print(len(set_forall_lang))
for i in set_forall_lang:
    print(i)

print(len(set_lang))
for i in set_lang:
    print(i)

