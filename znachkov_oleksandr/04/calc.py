RAWTEXT = """  "Coronavirus: Germany to centralize supply chains, set prices on masks, protective gear
The COVID-19 pandemic has led to global shortages of key protective supplies — and fraudsters looking to profit off the desperate need to procure them. Now Berlin is looking at ways to fill the gaps and combat extortion.

    
Woman in protective gear (picture-alliance/dpa/M. Kusch)
As the SARS-CoV-2 virus spreads globally and cases of the resulting COVID-19 disease multiply exponentially, shortages of surgical masks, as well as N95 and other particle-filtering respirator masks, protective gowns and scrubs, gloves and other key materials have been widely reported at hospitals treating the infected. Already in early February, the World Health Organization (WHO) warned that the world would soon face a global shortage.

Dieter Wallström, a hospital purchasing manager in northern Bavaria, told the German newspaper Süddeutsche Zeitung that in many hospitals he knows of, personnel are becoming "so desperate that they are buying nearly everything." The result of this, he said, is that already, "The market is going berserk, and the prices are becoming inflationary."

Wolfgang Appelstiel and Olaf Berse, who head the nationwide hospital supplier Clinicpartner, agree. The group, which supplies some 400 hospitals and clinics across Germany, has already seen a flood of dubious suppliers offering up all sorts of products, possibly counterfeit. "It is the Wild West" of purchasing, Berse told the Süddeutsche Zeitung.

The scope of the problem is wide enough that even Germany's foreign intelligence agency, BND, has warned that the risks to the health care sector due to "intransparent delivery chains" cannot be underestimated, according to media reports.

Read more: German doctors lay down life-or-death guidelines

Desperate times

The shortages have already become apparent at many clinics and hospitals in Germany, whose health system usually ranks as among the world's best. Many procurement directors have reported having no choice but to attempt to sterilize and re-use masks as they search desperately for suppliers.

But those supplying key products amid a pandemic may not all be on the level. There have been widespread reports of fake protective gear being sold, or the legitimate products simply disappearing before arrival — stolen by unscrupulous thieves looking to resell them at astronomical profits.

Read more: Europol warns against coronavirus scams

Europol, the EU's law enforcement agency, reported that one European firm ordered some €6.6 million ($7.3 million) worth of protective masks and disinfection gel from a company in Singapore — which never arrived. Likewise, a German government shipment of millions of masks from Kenya never turned up. And the Netherlands recently recalled millions of defective masks bought from China.

The market has been flooded with "counterfeit health and sanitary products" and even phony medications, said the police agency. In just one coordinated operation between March 3 and 10, Europol confiscated 34,000 counterfeit surgical masks.

Health Ministry steps in

Now, in light of calls for a central procurement authority, the German government has started an open process for tenders that would bypass administrative hurdles and speed up delivery. Under the process, suppliers must be able to supply a minimum of 25,000 pieces of either masks or gear, guarantee a minimum quality standard and arrange for delivery.

German Health Minister Jens Spahn has called for "other approaches and new partners" in order to better equip health care workers. On Sunday, Spahn confirmed to German newspaper Welt am Sonntag that his ministry was scaling up to nationwide procurement.

"We want to protect as best we can doctors, care workers, and all those who work in health entities. That is why we are purchasing medical protective gear at the federal government level and supplying it to all states and public health associations."

Spahn said that the approach would guarantee that, "We are offering fair, firm prices for all domestic and international suppliers of protective masks and gear."

German parliamentarian and health expert Karl Lauterbach, who had called for the measures, told the Süddeutsche Zeitung and public broadcasters WDR and NDR on Sunday that the measures were necessary, but he called for the government to go even further.

He said Berlin must "immediately establish a federal agency and task it with production and distribution" across Germany. The urgency and scale of the crisis "is not something that the market can solve," he said."
"""
EXCEPTION = ("a an to is are was were will would could and or if he she it this my offer").split()

def rempunctuation (text):
    retext = "" 
    for symbol in text:
        if symbol.isalpha() or symbol.isspace():
            retext += symbol

    return retext.split()

def filldict (list_):
    wdict = {}
    for word in list_:
        if word in EXCEPTION:
            continue
        if word not in wdict.keys():
            wdict[word] = 0 
            wdict[word] = wdict.get(word) + 1
        else:
            wdict[word] = wdict.get(word) + 1
    return wdict

def findtop (dict_):
    rdict = {}
    sorted_ = sorted (list (dict_.values()), reverse = True)
    for index in range (3):
        for key, value in dict_.items():
            if value == sorted_[index]:
                rdict[key] = value
    return rdict

def freq (dict_):
    size = len (dict_.values())
    print ("=============",size)
    for key, value in dict_.items():
        dict_[key] = value * 100 / size 
    return dict_


list_of_words = rempunctuation(RAWTEXT.lower()) 

print ("- words quantity:", len(list_of_words))

mydict = filldict (list_of_words)
print ("- text dictionary: ", end = '')

for word in mydict.keys():
    print (word ," ", end = '')

print ("")

print ("- keywords: ", end = "")
for key, value in (findtop (mydict)).items():
    print (key, "-", value, "", end = "")

print ("")

print ("- frequency:", end = "")
#print (freq (mydict))

for key, value in (freq (mydict)).items():
    print (key, "-", value, " " ,end = "")

print ("")
