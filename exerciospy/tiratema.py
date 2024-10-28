metro = float(input("Digite valor do metro a ser convertido, caso seja decimal, usar ponto (.) no lugar da vírgula (,): "))
dam = metro/10
hm = dam/10
km = hm/10
dm = metro*10
cm = dm*10
mm = cm * 10
print(f"""{metro:.4} metros -m- equivale a:
{dam:.4} decâmetro/s -dam-,
{hm:.4} hectômetro/s -hm-,
{km:.4} Quilômetro/s -km-,
{dm:.4} decímetro/s -dm-,
{cm:.4} centímetro/s -cm-,
{mm:.4} milímetro/s -m-.""")
