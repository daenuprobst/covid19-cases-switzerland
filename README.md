# covid19-cases-switzerland

New data is aggregated from:
[https://github.com/openZH/covid_19](https://github.com/openZH/covid_19)

Legacy data sources and credits:

- Official BAG [Twitter Account](https://twitter.com/BAG_OFSP_UFSP)
- BFS [Hospital Beds](https://www.bfs.admin.ch/bfs/de/home/statistiken/gesundheit/gesundheitswesen/spitaeler/infrastruktur-beschaeftigung-finanzen.assetdetail.10647166.html)
- Data for [NW](https://www.nw.ch/gesundheitsamtdienste/6044#Anzahl%C2%A0Erkrankungen)
- Data for [BE](https://www.besondere-lage.sites.be.ch/besondere-lage_sites/de/index/corona/index.html#originRequestUrl=www.be.ch/corona)
- Data for [SG](https://www.sg.ch/tools/informationen-coronavirus.html)
- Data for [TI](https://www4.ti.ch/area-media/comunicati/), Grazie [@sarahhu87422283](https://twitter.com/sarahhu87422283), Danke [vecirex](https://twitter.com/vecirex)
- Data for [NE](https://www.ne.ch/autorites/DFS/SCSP/medecin-cantonal/maladies-vaccinations/Pages/Coronavirus.aspx), Merci [@borisfritscher](https://twitter.com/borisfritscher)
- Data for [AG](https://www.ag.ch/de/themen_1/coronavirus_2/coronavirus.jsp), Danke [@BachliMeyer](https://twitter.com/BachliMeyer)
- Data for [GR](https://www.youtube.com/channel/UCEcqzK6vbCuIvxLiJCAMVuA)
- Data for [AI](https://www.ai.ch/themen/gesundheit-alter-und-soziales/gesundheitsfoerderung-und-praevention/uebertragbare-krankheiten/coronavirus), Danke [@BachliMeyer](https://twitter.com/BachliMeyer)
- Data for [UR](https://www.ur.ch/themen/2920),
- Data for [VS](https://www.vs.ch/de/web/coronavirus), Merci [@enno_hermann](https://twitter.com/enno_hermann)
- Data for [BS](https://www.coronavirus.bs.ch/)
- Data for [JU](https://www.jura.ch/fr/Autorites/Coronavirus/Accueil/Coronavirus-Informations-officielles-a-la-population-jurassienne.html)
- Data for [GE](https://www.ge.ch/covid-19-coronavirus-geneve/situation-epidemiologique-geneve) Merci [@ThomasGriessen](https://twitter.com/ThomasGriessen)
- Data for [LU](https://www.luzernerzeitung.ch/zentralschweiz/luzern/so-will-die-luzerner-regierung-die-massnahmen-des-bundes-umsetzen-lukb-stellt-50-millionen-franken-bereit-ld.1204954), Danke [@neph_b](https://twitter.com/neph_b) \*Data ard from the video.
- Data for [VD](https://www.vd.ch/toutes-les-actualites/hotline-et-informations-sur-le-coronavirus/point-de-situation-statistique-dans-le-canton-de-vaud/), Merci [@f_giroud](https://twitter.com/f_giroud)
- Data for [TG](https://www.tg.ch/news/fachdossier-coronavirus.html/10552), Danke [@KeveHilfi](https://twitter.com/KeveHilfi)
- Data for [ZH](https://github.com/openZH/covid_19), Danke, [@zdavatz](https://twitter.com/zdavatz)
- Data for [SH](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Departement-des-Innern/Gesundheitsamt-3209198-DE.html), Danke [@BachliMeyer](https://twitter.com/BachliMeyer)
- Data for [BL](https://www.baselland.ch/), Danke [@BachliMeyer](https://twitter.com/BachliMeyer), the MVP ;-)
- Data for [ZG](https://www.zg.ch/behoerden/gesundheitsdirektion/direktionssekretariat/aktuell/coronavirus-ausreichende-testkapazitaeten-im-kanton-zug-vorhanden)
- Data for [FR](https://www.fr.ch/covid19/sante/covid-19/coronavirus-statistiques-evolution-de-la-situation-dans-le-canton) Merci [@mtille](https://twitter.com/mtille)
- Data for [SO](https://corona.so.ch/), Danke [@fabiangysel1997](https://twitter.com/fabiangysel1997)
- Data for [AR](https://www.ar.ch/verwaltung/departement-gesundheit-und-soziales/amt-fuer-gesundheit/informationsseite-coronavirus/)
- Data for [ZG](https://www.zg.ch/behoerden/gesundheitsdirektion/amt-fuer-gesundheit/corona)
- Data for [GL](https://www.gl.ch/verwaltung/finanzen-und-gesundheit/gesundheit/coronavirus.html/4817#Fallzahlen), Danke [@fabiangysel1997](https://twitter.com/fabiangysel1997)
- Data for [OW](https://www.ow.ch/de/verwaltung/dienstleistungen/?dienst_id=5962#Generelle%20Informationen), Danke [@fabiangysel1997](https://twitter.com/fabiangysel1997)

- Important: The data for 18. 03. 2020 has been calculated from the incidence data [published by the BAG](https://www.bag.admin.ch/dam/bag/de/dokumente/mt/k-und-i/aktuelle-ausbrueche-pandemien/2019-nCoV/covid-19-lagebericht.pdf.download.pdf/COVID-19_Epidemiologische_Lage_Schweiz.pdf). However, this data seems to be outdated or based on different population numbers than the data from the 2018 census I used. However, the latter is rather unlikely. I have thus merged all values from the BAG that are HIGHER than those from the cantonal sources into the table. This will continue for future data as well.

- BL has added an [interactive plot](https://www.baselland.ch/politik-und-behorden/direktionen/volkswirtschafts-und-gesundheitsdirektion/amt-fur-gesundheit/medizinische-dienste/kantonsarztlicher-dienst/aktuelles/covid-19-faelle-kanton-basel-landschaft) to their website, great work!

Preliminary diagnoses (not confirmed by Geneva) are counted as cases.

There are missing numbers now. I suggest to either get them via fitting or interpolation.

## Interactive Dashboard

- https://www.corona-data.ch

## Map Overview of Swiss data

- http://corona-ch.surge.sh/
