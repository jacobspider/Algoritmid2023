Funktsioon Hüpikotsing(massiiv, otsitav_element)
n = massiivi_pikkus
hype = floor(sqrt(n))
eelmine = 0

#hüppa sammude kaupa kuni leitakse blokk
while massiiv[min(hype, n)- 1] < otsitav_elemnt:
    eelmine = hype
    samm += floor(sqrt(n))
    kui eelmine >= n:
        #elementi ei ole
        tagasta -1
    

for i vahemikus [eelmine, min(hype, n)]:
    kui massiiv[i] == otsitav_element:
        tagasta i
#elementi ei ole
tagasta -1