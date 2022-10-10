program asd_meangwa
function isSimetris (l: List) -> boolean
{
I.S. belum ereksi
F.S. crot ndak karuan
}
kamus lokal
	i: integer {iterator} { asd asd asd}
	len: integer {panjang list l}
	isValid: boolean {variabel status validitas}
algoritma
	isValid <- true
	i traversal [0 .. l.nEff/2]
		if l.contents[i] != l.contents[l.nEff - i - 1]
			isValid <- false 
	-> isValid
	
function plusTab (l1, l2: List, b : integer) -> List
kamus lokal
	asd, outl: List {penampung output}
	i: integer {iterator}
	p: integer {panjang list terpanjang}
algoritma
	CreateTable(outl)
	if l1.nEff > l2.nEff then
		p <- l1.nEff - 1
	else 
		p <- l2.nEff - 1.2
	i traversal [0 .. p]
		outl.contents[i] <- l1.contents[i] + l2.contents[i]
	output(i)
	-> outl 

procedure asd(input a: integer, output c: integer)
kamus lokal
	asd: integer
algoritma
	asd <- p mew_mew
	panjang <- asd


procedure asdsd( y)