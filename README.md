![Hard to be a god](images/misc/pateras.png)

Modeling Coups and Other Violent Power Transitions

#Summary:

#The Data

I used the REIGN dataset (see citation below) from One Earth Future for details on country leaders, government types, and when successful and attempted coups occured. I supplemented this with indicators from the World Bank and 

I created a data cleaning pipeline to process the different data sources

# EDA (Describe Characteristics of the Dataset)

![coups by country](images/coupsbycountry.png)

![coups by governments](images/coupsbygovttotal.png)

![coups by governments %](images/coupsbygovtpercent.png)

![coups by leader tenure](images/coupsbyleadertenure.png)

![coups by year](images/coupsyearly.png)




# Modeling: 

- Logistic Regression

- Random Forest

- XGboost

# Future Steps



#Citations:

##REIGN Dataset:

Bell, Curtis. 2016. The Rulers, Elections, and Irregular Governance Dataset (REIGN). Broomfield, CO: OEF Research. Available at oefresearch.org

The REIGN Dataset was constructed using the following resources:

Goemans, Henk E., Kristian Skrede Gleditch, and Giacomo Chiozza. 2009. "Introducing Archigos: A Dataset of Political Leaders" Journal of Peace Research, 46(2): 269-183. {{http://privatewww.essex.ac.uk/~ksg/archigos.html}}

Ellis, Cali Mortenson, Michael C. Horowitz, and Allan C. Stam. 2015. "Introducing the LEAD Data Set." International Interactions, 41(4): 718-741. {{http://www.tandfonline.com/doi/abs/10.1080/03050629.2015.1016157}}

Marshall, Monty G., Ted Robert Gurr, and Keith Jaggers. 2016. Polity IV Project. Center for Systemic Peace. {{http://www.systemicpeace.org/inscr/p4manualv2015.pdf}}

Barbara Geddes, Joseph Wright, and Erica Frantz. 2014. “Autocratic Regimes and Transitions.” Perspectives on Politics. 12(2).{{http://dictators.la.psu.edu/}}

Powell, Jonathan & Clayton Thyne. 2011. Global Instances of Coups from 1950-Present. Journal of Peace Research 48(2):249-259.{{http://www.jonathanmpowell.com/coup-detat-dataset.html}}

Erik Melander, Therése Pettersson, and Lotta Themnér (2016) Organized violence, 1989–2015. Journal of Peace Research 53(5) {{http://www.pcr.uu.se/research/ucdp/datasets/replication_datasets/}}

## Correlates of War Datasets

Colonial Contiguity:

Correlates of War Project. Colonial Contiguity Data, 1816-2016. Version 3.1. 

Military Alliances:

Gibler, Douglas M. 2009. International military alliances, 1648-2008. CQ Press.  

Dyadic Trade:

Barbieri, Katherine and Omar M. G. Omar Keshk. 2016. Correlates of War Project Trade Data Set Codebook, Version 4.0. Online: http://correlatesofwar.org. 

Barbieri, Katherine, Omar M. G. Keshk, and Brian Pollins. 2009. “TRADING DATA: Evaluating our Assumptions and Coding Rules.” Conflict Management and Peace Science. 26(5): 471-491.

Religion: 

 Zeev Maoz and Errol A. Henderson. 2013. “The World Religion Dataset, 1945-2010: Logic, Estimates, and Trends.” International Interactions, 39: 265-291. 

Militarized Interstate Dispute Locations

 Braithwaite, A. 2010. “MIDLOC: Introducing the Militarized Interstate Dispute (MID) Location Dataset.” Journal of Peace Research 47(1): 91-98.

Bezerra, P., & Braithwaite, A. 2019. Codebook for the Militarized Interstate Dispute Location (MIDLOC-A/I) Dataset, v2.1.
