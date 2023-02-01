---
title: "Data Dictionary Group 3"
output:
  html_document:
    df_print: paged
  pdf_document: default
---

```{r setup, include=FALSE}
S2<-read.csv(file="export_dataframe_stage2.csv")

library(dplyr)
library(ggplot2)
library(plotly)

g3<-S2%>%select(do_saturation,reagent,reagent_other,ph1,ph2,DissolvedOxygen1,DissolvedOxygen2,Conductivity,Salinity1,Salinity2,SecchiDisk1,SecchiDisk2,ChlorophyllA,Alkalinity,AmmoniaN,NitrateN,Turbidity,Orthophosphate,SamplingDepth,SettleableSolids,Chloride,Hardness)

numdeci <- function(x) {
    if ((x %% 1) != 0) {
        nchar(strsplit(sub('0+$', '', as.character(x)), ".", fixed=TRUE)[[1]][[2]])
    } else {
        return(0)
    }
}

testingdata<-g3
```
# do_saturation

#### Data Type
numeric

#### Units/Type of Data
percentage

#### Typical Ranges
80-100 
(https://www.enr.gov.nt.ca/sites/enr/files/dissolved_oxygen.pdf)

#### Description
Healthy water should generally have dissolved oxygen concentrations above 6.5-8 mg/L and between about 80-120%.

```{r}
AB_do_saturation<-filter(g3, do_saturation>120|do_saturation<80)
AB_do_saturation

DS_total<-summarize(g3,total=n())
DS_NA<-filter(g3, is.na(do_saturation) )%>%
  summarize(num_na=n())
DS_blank<-filter(g3, do_saturation=="" )%>%
  summarize(num_Blank=n())
DS_above<-filter(g3, do_saturation>120 )%>%
  summarize(num_above=n())
DS_below<-filter(g3, do_saturation<80 )%>%
  summarize(num_below=n())
DS_percentNA<-filter(g3, is.na(do_saturation) )%>%
  summarize(percent_na=n()/DS_total$total)
DS_min<-summarize(g3,min=min(do_saturation,na.rm=TRUE))
DS_max<-summarize(g3,max=max(do_saturation,na.rm=TRUE))
DS_implausible<-filter(g3,do_saturation<0)%>%
  summarize(below_zero=n())
DS<-data.frame(DS_total,DS_NA,DS_percentNA,DS_blank,DS_above,DS_below,DS_min,DS_max,DS_implausible)
DS
```



# reagent
#### Data Type
factor

#### Units/Type of Data
individual notes

#### Typical Ranges
NA

#### Description
Description of what type of reagents are present in the water sample

```{r}
summary(g3$reagent)
```


# reagent_other
#### Data Type
factor

#### Units/Type of Data
individual notes

#### Typical Ranges
NA

#### Description
Description of additional materials that may be required or other issues found with the sample

```{r}
head(g3$reagent_other)
```


# ph1
#### Data Type
numeric

#### Units/Type of Data
scale of 0-14

#### Typical Ranges
0-14

#### Description
pH is a unit of measure which describes the degree of acidity or alkalinity of a solution

```{r}
AB_ph1<-filter(g3, ph1>14|ph1<0 )
AB_ph1

PH1_total<-summarize(g3,total=n())
PH1_NA<-filter(g3, is.na(ph1) )%>%
  summarize(num_na=n())
PH1_blank<-filter(g3, ph1=="" )%>%
  summarize(num_Blank=n())
PH1_above<-filter(g3, ph1>14 )%>%
  summarize(num_above=n())
PH1_below<-filter(g3, ph1<0 )%>%
  summarize(num_below=n())
PH1_percentNA<-filter(g3, is.na(ph1) )%>%
  summarize(percent_na=n()/PH1_total$total)
PH1_min<-summarize(g3,min=min(ph1,na.rm=TRUE))
PH1_max<-summarize(g3,max=max(ph1,na.rm=TRUE))
PH1_implausible<-filter(g3,ph1<0)%>%
  summarize(below_zero=n())
PH1<-data.frame(PH1_total,PH1_NA,PH1_percentNA,PH1_blank,PH1_above,PH1_below,PH1_min,PH1_max,PH1_implausible)
PH1
```

# ph2
#### Data Type
numeric

#### Units/Type of Data
scale of 0-14

#### Typical Ranges
0-14

#### Description
pH is a unit of measure which describes the degree of acidity or alkalinity of a solution

```{r}
AB_ph2<-filter(g3, ph2>14|ph2<0 )
AB_ph2

PH2_total<-summarize(g3,total=n())
PH2_NA<-filter(g3, is.na(ph2) )%>%
  summarize(num_na=n())
PH2_blank<-filter(g3, ph2=="" )%>%
  summarize(num_Blank=n())
PH2_above<-filter(g3, ph2>14 )%>%
  summarize(num_above=n())
PH2_below<-filter(g3, ph2<0 )%>%
  summarize(num_below=n())
PH2_percentNA<-filter(g3, is.na(ph2) )%>%
  summarize(percent_na=n()/PH2_total$total)
PH2_min<-summarize(g3,min=min(ph2,na.rm=TRUE))
PH2_max<-summarize(g3,max=max(ph2,na.rm=TRUE))
PH2_implausible<-filter(g3,ph2<0)%>%
  summarize(below_zero=n())
PH2<-data.frame(PH2_total,PH2_NA,PH2_percentNA,PH2_blank,PH2_above,PH2_below,PH2_min,PH2_max,PH2_implausible)
PH2
```

# Compare ph1 and ph2
```{r}
# 1. both null
a<-g3%>%
  filter((is.na(ph1)) & (is.na(ph2)))%>%
  summarize(both_null=n())
# 2. both not null
b<-g3%>%
  filter((!is.na(ph1)) & (!is.na(ph2)))%>%
  summarize(both_not_null=n())
# 3. first null only
c<-g3%>%
  filter((is.na(ph1)) & (!is.na(ph2)))%>%
  summarize(first_null_only=n())
# 4. second null only
d<-g3%>%
  filter((!is.na(ph1)) & (is.na(ph2)))%>%
  summarize(second_null_only=n())
# 5.total
e<-g3%>%
  summarize(total=n())
ph_12=data.frame(a,b,c,d,e)
ph_12
```


# DissolvedOxygen1
#### Data Type
numeric

#### Units/Type of Data
concentration: mg/L

#### Typical Ranges
5-12
(https://www.ysi.com/File%20Library/Documents/Application%20Notes/A564-02-Dissolved-Oxygen-in-Aquaculture-Ponds-5-.pdf)

#### Description
The amount of dissolved oxygen per liter of water

```{r}
AB_DissolvedOxygen1<-filter(g3, DissolvedOxygen1>12|DissolvedOxygen1<5 )
AB_DissolvedOxygen1

DO1_total<-summarize(g3,total=n())
DO1_NA<-filter(g3, is.na(DissolvedOxygen1) )%>%
  summarize(num_na=n())
DO1_blank<-filter(g3, DissolvedOxygen1=="" )%>%
  summarize(num_Blank=n())
DO1_above<-filter(g3, DissolvedOxygen1>12 )%>%
  summarize(num_above=n())
DO1_below<-filter(g3, DissolvedOxygen1<5 )%>%
  summarize(num_below=n())
DO1_percentNA<-filter(g3, is.na(DissolvedOxygen1) )%>%
  summarize(percent_na=n()/DO1_total$total)
DO1_min<-summarize(g3,min=min(DissolvedOxygen1,na.rm=TRUE))
DO1_max<-summarize(g3,max=max(DissolvedOxygen1,na.rm=TRUE))
DO1_implausible<-filter(g3,DissolvedOxygen1<0)%>%
  summarize(below_zero=n())
DO1<-data.frame(DO1_total,DO1_NA,DO1_percentNA,DO1_blank,DO1_above,DO1_below,DO1_min,DO1_max,DO1_implausible)
DO1
```


# DissolvedOxygen2
#### Data Type
numeric

#### Units/Type of Data
concentration: mg/L

#### Typical Ranges
5-12
(https://www.ysi.com/File%20Library/Documents/Application%20Notes/A564-02-Dissolved-Oxygen-in-Aquaculture-Ponds-5-.pdf)

#### Description
The amount of dissolved oxygen per liter of water

```{r}
AB_DissolvedOxygen2<-filter(g3, DissolvedOxygen2>12|DissolvedOxygen2<5 )
AB_DissolvedOxygen2

DO2_total<-summarize(g3,total=n())
DO2_NA<-filter(g3, is.na(DissolvedOxygen2) )%>%
  summarize(num_na=n())
DO2_blank<-filter(g3, DissolvedOxygen2=="" )%>%
  summarize(num_Blank=n())
DO2_above<-filter(g3, DissolvedOxygen2>12 )%>%
  summarize(num_above=n())
DO2_below<-filter(g3, DissolvedOxygen2<5 )%>%
  summarize(num_below=n())
DO2_percentNA<-filter(g3, is.na(DissolvedOxygen2) )%>%
  summarize(percent_na=n()/DO2_total$total)
DO2_min<-summarize(g3,min=min(DissolvedOxygen2,na.rm=TRUE))
DO2_max<-summarize(g3,max=max(DissolvedOxygen2,na.rm=TRUE))
DO2_implausible<-filter(g3,DissolvedOxygen2<0)%>%
  summarize(below_zero=n())
DO2<-data.frame(DO2_total,DO2_NA,DO2_percentNA,DO2_blank,DO2_above,DO2_below,DO2_min,DO2_max,DO2_implausible)
DO2
```

# Compare DissolvedOxygen1 and DissolvedOxygen2
```{r}
# 1. both null
a<-g3%>%
  filter((is.na(DissolvedOxygen1)) & (is.na(DissolvedOxygen2)))%>%
  summarize(both_null=n())
# 2. both not null
b<-g3%>%
  filter((!is.na(DissolvedOxygen1)) & (!is.na(DissolvedOxygen2)))%>%
  summarize(both_not_null=n())
# 3. first null only
c<-g3%>%
  filter((is.na(DissolvedOxygen1)) & (!is.na(DissolvedOxygen2)))%>%
  summarize(first_null_only=n())
# 4. second null only
d<-g3%>%
  filter((!is.na(DissolvedOxygen1)) & (is.na(DissolvedOxygen2)))%>%
  summarize(second_null_only=n())
# 5.total
e<-g3%>%
  summarize(total=n())
DissolvedOxygen_12=data.frame(a,b,c,d,e)
DissolvedOxygen_12
```

```{r}
#create table with DO1, DO2, and difference between D01 and DO2
compareDO<-g3%>%
  filter((!is.na(DissolvedOxygen1)) & (!is.na(DissolvedOxygen2)))%>%
  select("DissolvedOxygen1","DissolvedOxygen2")%>%
  mutate(Difference=DissolvedOxygen1-DissolvedOxygen2)
compareDO

#Describe difference between DO1 and DO2
summary(compareDO$Difference) #range is -5.20000 to 8.20000
sum(compareDO$Difference!=0)/length(compareDO$Difference) #35.74% of filled entries do not match between DO1 and DO2

ggplot(compareDO, aes(x=Difference)) + geom_histogram(color="black", fill="gray", binwidth = 0.25) #visualization of all the differences
```

# Conductivity
#### Data Type
numeric

#### Units/Type of Data
micromhos per centimeter (µmhos/cm)

#### Typical Ranges
Distilled water: 0.5 to 3 µmhos/cm. 
US rivers: 50 to 1500 µmhos/cm. 
Inland fresh waters: 150 and 500 µhos/cm. 
Industrial waters can range as high as 10,000 µmhos/cm.
https://archive.epa.gov/water/archive/web/html/vms59.html#:~:text=Conductivity%20is%20measured%20with%20a,calculate%20the%20conductivity%20per%20centimeter. 

#### Description
Conductivity: measure of water’s ability to conduct electrical current.

```{r}
Con_total<-summarize(g3,total=n())
Con_NA<-filter(g3, is.na(Conductivity) )%>%
  summarize(num_na=n())
Con_blank<-filter(g3, Conductivity=="" )%>%
  summarize(num_Blank=n())
Con_above<-filter(g3, Conductivity>1500 )%>%
  summarize(num_above=n())
Con_below<-filter(g3, Conductivity<50 )%>%
  summarize(num_below=n())
Con_percentNA<-filter(g3, is.na(Conductivity) )%>%
  summarize(percent_na=n()/Con_total$total)
Con_min<-summarize(g3,min=min(Conductivity,na.rm=TRUE))
Con_max<-summarize(g3,max=max(Conductivity,na.rm=TRUE))
Con_implausible<-filter(g3,Conductivity<0)%>%
  summarize(below_zero=n())
Con<-data.frame(Con_total,Con_NA,Con_percentNA,Con_blank,Con_above,Con_below,Con_min,Con_max,Con_implausible)
Con
```
Maximum value is 400,000. 

# Salinity1
#### Data Type
numeric

#### Units/Type of Data
Concentration: ppt

#### Typical Ranges
Fresh water: Less than 1 ppt
Slightly saline water: 1 ppt to 3 ppt
Moderately saline water: 3 ppt to 10 ppt
Highly saline water: 10 ppt to 35 ppt
Ocean: 35,000 ppm 
https://www.usgs.gov/special-topics/water-science-school/science/saline-water-and-salinity 

#### Description
Measurement of dissolved salts in water
```{r}
Sal1_total<-summarize(g3,total=n())
Sal1_NA<-filter(g3, is.na(Salinity1) )%>%
  summarize(num_na=n())
Sal1_blank<-filter(g3, Salinity1=="" )%>%
  summarize(num_Blank=n())
Sal1_fresh<-filter(g3, Salinity1>0 & Salinity1<1)%>%
  summarize(num_fresh=n())
Sal1_slight<-filter(g3, Salinity1>=1 & Salinity1<3)%>%
  summarize(num_slight=n())
Sal1_moderate<-filter(g3, Salinity1>=3 & Salinity1<10)%>%
  summarize(num_moderate=n())
Sal1_high<-filter(g3, Salinity1>=10 & Salinity1<35)%>%
  summarize(num_high=n())
Sal1_ocean<-filter(g3, Salinity1>=35)%>%
  summarize(num_ocean=n())
Sal1_percentNA<-filter(g3, is.na(Salinity1) )%>%
  summarize(percent_na=n()/Sal1_total$total)
Sal1_min<-summarize(g3,min=min(Salinity1,na.rm=TRUE))
Sal1_max<-summarize(g3,max=max(Salinity1,na.rm=TRUE))
Sal1_implausible<-filter(g3,Salinity1<0)%>%
  summarize(below_zero=n())
Sal1<-data.frame(Sal1_total,Sal1_NA,Sal1_percentNA,Sal1_blank,Sal1_fresh,Sal1_slight,Sal1_moderate,Sal1_high,Sal1_ocean,Sal1_min,Sal1_max,Sal1_implausible)
Sal1

```


# Salinity2
#### Data Type
numeric

#### Units/Type of Data
Concentration: ppt

#### Typical Ranges
Fresh water: Less than 1 ppt
Slightly saline water: 1 ppt to 3 ppt
Moderately saline water: 3 ppt to 10 ppt
Highly saline water: 10 ppt to 35 ppt
Ocean: 35,000 ppm 
https://www.usgs.gov/special-topics/water-science-school/science/saline-water-and-salinity 

#### Description
Measurement of dissolved salts in water

```{r}
Sal2_total<-summarize(g3,total=n())
Sal2_NA<-filter(g3, is.na(Salinity2) )%>%
  summarize(num_na=n())
Sal2_blank<-filter(g3, Salinity2=="" )%>%
  summarize(num_Blank=n())
Sal2_fresh<-filter(g3, Salinity2>0 & Salinity2<1)%>%
  summarize(num_fresh=n())
Sal2_slight<-filter(g3, Salinity2>=1 & Salinity2<3)%>%
  summarize(num_slight=n())
Sal2_moderate<-filter(g3, Salinity2>=3 & Salinity2<10)%>%
  summarize(num_moderate=n())
Sal2_high<-filter(g3, Salinity2>=10 & Salinity2<35)%>%
  summarize(num_high=n())
Sal2_ocean<-filter(g3, Salinity2>=35)%>%
  summarize(num_ocean=n())
Sal2_percentNA<-filter(g3, is.na(Salinity2) )%>%
  summarize(percent_na=n()/Sal2_total$total)
Sal2_min<-summarize(g3,min=min(Salinity2,na.rm=TRUE))
Sal2_max<-summarize(g3,max=max(Salinity2,na.rm=TRUE))
Sal2_implausible<-filter(g3,Salinity2<0)%>%
  summarize(below_zero=n())
Sal2<-data.frame(Sal2_total,Sal2_NA,Sal2_percentNA,Sal2_blank,Sal2_fresh,Sal2_slight,Sal2_moderate,Sal2_high,Sal2_ocean,Sal2_min,Sal2_max,Sal2_implausible)
Sal2
```


# Compare Salinity1 and Salinity2
```{r}
# 1. both null
a<-g3%>%
  filter((is.na(Salinity1)) & (is.na(Salinity2)))%>%
  summarize(both_null=n())
# 2. both not null
b<-g3%>%
  filter((!is.na(Salinity1)) & (!is.na(Salinity2)))%>%
  summarize(both_not_null=n())
# 3. first null only
c<-g3%>%
  filter((is.na(Salinity1)) & (!is.na(Salinity2)))%>%
  summarize(first_null_only=n())
# 4. second null only
d<-g3%>%
  filter((!is.na(Salinity1)) & (is.na(Salinity2)))%>%
  summarize(second_null_only=n())
# 5.total
e<-g3%>%
  summarize(total=n())
Salinity_12=data.frame(a,b,c,d,e)
Salinity_12
```


# SecchiDisk1
#### Data Type
numeric

#### Units/Type of Data
Depth: meters

#### Typical Ranges
Secchi depth can range from centimeters to > 40 m. Typical depths range from 2-10 meters. 
https://web.uri.edu/watershedwatch/files/Secchi.pdf

#### Description
Measuring Secchi Depth (how far a Secchi Disk is lowered before it no longer can be visually observed), which is an indication of the transparency of the water. 
```{r}
SD1_total<-summarize(g3,total=n())
SD1_NA<-filter(g3, is.na(SecchiDisk1) )%>%
  summarize(num_na=n())
SD1_blank<-filter(g3, SecchiDisk1=="" )%>%
  summarize(num_Blank=n())
SD1_above<-filter(g3, SecchiDisk1>200 )%>%
  summarize(num_above=n())
SD1_below<-filter(g3, SecchiDisk1<20 )%>%
  summarize(num_below=n())
SD1_percentNA<-filter(g3, is.na(SecchiDisk1) )%>%
  summarize(percent_na=n()/SD1_total$total)
SD1_min<-summarize(g3,min=min(SecchiDisk1,na.rm=TRUE))
SD1_max<-summarize(g3,max=max(SecchiDisk1,na.rm=TRUE))
SD1_implausible<-filter(g3,SecchiDisk1<0)%>%
  summarize(below_zero=n())
SD1<-data.frame(SD1_total,SD1_NA,SD1_percentNA,SD1_blank,SD1_above,SD1_below,SD1_min,SD1_max,SD1_implausible)
SD1
```


# SecchiDisk2
#### Data Type
numeric

#### Units/Type of Data
Depth: meters

#### Typical Ranges
Secchi depth can range from centimeters to > 40 m. Typical depths range from 2-10 meters. 
https://web.uri.edu/watershedwatch/files/Secchi.pdf

#### Description
Measuring Secchi Depth (how far a Secchi Disk is lowered before it no longer can be visually observed), which is an indication of the transparency of the water. 
```{r}
SD2_total<-summarize(g3,total=n())
SD2_NA<-filter(g3, is.na(SecchiDisk2) )%>%
  summarize(num_na=n())
SD2_blank<-filter(g3, SecchiDisk2=="" )%>%
  summarize(num_Blank=n())
SD2_above<-filter(g3, SecchiDisk2>200 )%>%
  summarize(num_above=n())
SD2_below<-filter(g3, SecchiDisk2<20 )%>%
  summarize(num_below=n())
SD2_percentNA<-filter(g3, is.na(SecchiDisk2) )%>%
  summarize(percent_na=n()/SD2_total$total)
SD2_min<-summarize(g3,min=min(SecchiDisk2,na.rm=TRUE))
SD2_max<-summarize(g3,max=max(SecchiDisk2,na.rm=TRUE))
SD2_implausible<-filter(g3,SecchiDisk2<0)%>%
  summarize(below_zero=n())
SD2<-data.frame(SD2_total,SD2_NA,SD2_percentNA,SD2_blank,SD2_above,SD2_below,SD2_min,SD2_max,SD2_implausible)
SD2
```


# Compare SecchiDisk1 and SecchiDisk2
```{r}
# 1. both null
a<-g3%>%
  filter((is.na(SecchiDisk1)) & (is.na(SecchiDisk2)))%>%
  summarize(both_null=n())
# 2. both not null
b<-g3%>%
  filter((!is.na(SecchiDisk1)) & (!is.na(SecchiDisk2)))%>%
  summarize(both_not_null=n())
# 3. first null only
c<-g3%>%
  filter((is.na(SecchiDisk1)) & (!is.na(SecchiDisk2)))%>%
  summarize(first_null_only=n())
# 4. second null only
d<-g3%>%
  filter((!is.na(SecchiDisk1)) & (is.na(SecchiDisk2)))%>%
  summarize(second_null_only=n())
# 5.total
e<-g3%>%
  summarize(total=n())
SecchiDisk_12=data.frame(a,b,c,d,e)
SecchiDisk_12
```


# ChlorophyllA
#### Data Type
numeric

#### Units/Type of Data
Concentration: mg/L

#### Typical Ranges
Freshwater lakes range from 1-300 mg/L
https://www.geog.ucl.ac.uk/resources/laboratory/laboratory-methods/water-analysis/chlorophyll-a-concentration#:~:text=The%20value%2011.0%20is%20derived,range%201%20%2D%20300mg%2FL. 

#### Description
Chlorophyll a is a substance that allows plants to photosynthesize. It is a measure of the amount of algae growing in a waterbody.
https://www.epa.gov/national-aquatic-resource-surveys/indicators-chlorophyll#:~:text=Chlorophyll%20a%20is%20a%20measure,trophic%20condition%20of%20a%20waterbody. 
```{r}
CA_total<-summarize(g3,total=n())
CA_NA<-filter(g3, is.na(ChlorophyllA) )%>%
  summarize(num_na=n())
CA_blank<-filter(g3, ChlorophyllA=="" )%>%
  summarize(num_Blank=n())
CA_above<-filter(g3, ChlorophyllA>200 )%>%
  summarize(num_above=n())
CA_below<-filter(g3, ChlorophyllA<20 )%>%
  summarize(num_below=n())
CA_percentNA<-filter(g3, is.na(ChlorophyllA) )%>%
  summarize(percent_na=n()/CA_total$total)
CA_min<-summarize(g3,min=min(ChlorophyllA,na.rm=TRUE))
CA_max<-summarize(g3,max=max(ChlorophyllA,na.rm=TRUE))
CA_implausible<-filter(g3,ChlorophyllA<0)%>%
  summarize(below_zero=n())
CA<-data.frame(CA_total,CA_NA,CA_percentNA,CA_blank,CA_above,CA_below,CA_min,CA_max,CA_implausible)
CA
```


# Alkalinity 
#### Data Type
numeric

#### Units/Type of Data
concentration: ppm

#### Typical Ranges
20-200

#### Description
Alkalinity is the strength of a buffer solution composed of weak acids and their conjugate bases.
```{r}
AB_Alkalinity<-filter(g3, Alkalinity>200|Alkalinity<20 )
AB_Alkalinity

AK_total<-summarize(g3,total=n())
AK_NA<-filter(g3, is.na(Alkalinity) )%>%
  summarize(num_na=n())
AK_blank<-filter(g3, Alkalinity=="" )%>%
  summarize(num_Blank=n())
AK_above<-filter(g3, Alkalinity>200 )%>%
  summarize(num_above=n())
AK_below<-filter(g3, Alkalinity<20 )%>%
  summarize(num_below=n())
AK_percentNA<-filter(g3, is.na(Alkalinity) )%>%
  summarize(percent_na=n()/AK_total$total)
AK_min<-summarize(g3,min=min(Alkalinity,na.rm=TRUE))
AK_max<-summarize(g3,max=max(Alkalinity,na.rm=TRUE))
AK_implausible<-filter(g3,Alkalinity<0)%>%
  summarize(below_zero=n())
AK<-data.frame(AK_total,AK_NA,AK_percentNA,AK_blank,AK_above,AK_below,AK_min,AK_max,AK_implausible)
AK
```


# AmmoniaN
#### Data Type
numeric

#### Units/Type of Data
Concentration: mg/L

#### Typical Ranges
Environmental limits: 0.25 to 32.5 mg/l
Standard for drinking water: 0.5, according to National Academy of Sciences
#### Description
Ammonia: a chemical compound containing nitrogen; water pollutant
https://www.oregon.gov/oha/ph/HealthyEnvironments/DrinkingWater/Monitoring/Documents/health/ammonia.pdf 
```{r}
class(g3$AmmoniaN)
sum(is.na(g3$AmmoniaN))
length(g3$AmmoniaN)-sum(is.na(g3$AmmoniaN))
summary(g3$AmmoniaN)
sum(g3$AmmoniaN<0.25, na.rm=T)
```
* Data type: numeric
* NA values: 58625
* Number of input values: 973
* Range: 0 to 10
* Values outside typical range: 
  * Less than 0.25: 913
* Implausible values
  * none
* Only integers?: no, 2 decimal places
```{r}
#Distribution of Ammonia
ggplot(g3, aes(x=AmmoniaN)) + geom_histogram(color="black", fill="gray")
```

# NitrateN
#### Data Type
numeric

#### Units/Type of Data
Concentration: mg/L

#### Typical Ranges
Low level: <3 mg/L
Upper limit: 10  mg/L
https://www.health.state.mn.us/communities/environment/water/contaminants/nitrate.html#Background 

#### Description
Nitrate: a chemical compound containing nitrogen; water pollutant 

```{r}
summary(g3$NitrateN)
str(g3$NitrateN)
sum(is.na(g3$NitrateN))
sum(is.na(g3$NitrateN))/length(g3$NitrateN)
sum(g3$NitrateN<0,na.rm=T)
sum(g3$NitrateN>0 & g3$NitrateN<3,na.rm=T)
sum(g3$NitrateN>10,na.rm=T)
```
* There are 67 values in which the concentration of Nitrate is recorded as less than zero. This is not plausible. 
* 2765 entries fall below the typical lower limit of 3 mg/L.
* There are 54 values in which the concentration is recorded as greater than 10. While this is plausible, it is entering dangerous levels. 
* 53406 NA values. 
* 89.61% are NA values 
```{r}
#Distribution of Nitrate
ggplot(g3, aes(x=NitrateN)) + geom_histogram(color="black", fill="gray")
```

# Compare ammonia and nitrate
```{r}
AmNit<-ggplot(g3, aes(x=log(NitrateN),y=log(AmmoniaN))) + geom_point()
              
ggplotly(AmNit)
```

# Orthophosphate
#### Data Type
numeric
#### Units/Type of Data
concentration: mg/L
#### Typical Ranges
1-3.5 mg/L
https://archive.theincline.com/2018/09/27/10-things-you-need-to-know-about-orthophosphate-coming-soon-to-pittsburgh-drinking-water/#:~:text=Dzombak%20added%3A%20%E2%80%9CThe%20dosing%20range,on%20the%20particular%20water%20chemistry.

#### Description
Orthophosphate: water treatment agent coating pipes that reduces lead levels in water

```{r}
class(g3$Orthophosphate)
sum(is.na(g3$Orthophosphate))/length(g3$Orthophosphate)
summary(g3$Orthophosphate)
sum(g3$Orthophosphate<0,na.rm=T)
sum(g3$Orthophosphate>0 & g3$Orthophosphate<1,na.rm=T)
sum(g3$Orthophosphate>3.5,na.rm=T)
```
* Data type: numeric
* NA values: 53623
* Percentage of NA: 89.97%
* Range: -1 to 100
* Values outside typical range: 
  * Less than 1: 2211
  * Greater than 3.5: 68
* Implausible values: none
  * Less than 0: 78
* Only integers?: no, 2 decimal places
```{r}
Ortho<-ggplot(g3, aes(x=Orthophosphate)) + geom_histogram(color="black", fill="gray")
Ortho
```

# SamplingDepth
#### Data Type
numeric
#### Units/Type of Data
Depth: meters
#### Typical Ranges
#### Description
How deep the water sample is collected.
```{r}
class(g3$SamplingDepth)
sum(is.na(g3$SamplingDepth))
length(g3$SamplingDepth)-sum(is.na(g3$SamplingDepth))
summary(g3$SamplingDepth)
```
* Data type: numeric
* NA values: 59270
* Number of inputs: 328
* Range: 0 to 125
* Values outside typical range: none
* Implausible values: none
* Only integers?: no, 2 decimal places
```{r}
SDepth<-ggplot(g3, aes(x=SamplingDepth)) + geom_histogram(color="black", fill="gray")
SDepth
```

# SettleableSolids
** Background: **
  *Volume measure in mL/L
  * Typical Ranges: 
  * Description:
    * solid matter found in water that settles to the bottom of a container
```{r}
class(g3$SettleableSolids) #factor
sum(is.na(g3$SettleableSolids)) 
summary(g3$SettleableSolids) 
levels(g3$SettleableSolids) #others not included
sum(g3$SettleableSolids=="",na.rm=T) #find missing values
```
* Data type: factor
* NA values: 0
* Range: 
* Missing Values:  54902 
* Some entries are listed as "Trace"
  * All other values are numeric
* Implausible values
  * Less than 0: 106 values

# Turbidity
** Background: **
  * measured in Nephelometric Turbidity Units (NTU)
  * Typical Ranges: 
    *According to Alaska’s Water Quality Standards regulations at 18 AAC 70.020, when the natural turbidity of water is 50 NTU or less, human-caused turbidity may not surpass 5 NTU above natural conditions. 
    * When natural turbidity is 50 NTU or less, human-caused turbidity may not result in more than a 10% increase in turbidity. 
    * Meters can measure from 0-1000 NTU. 
    * https://archive.epa.gov/water/archive/web/html/vms55.html 
  * Description:
    * Turbidity: measure of water clarity, suspended solid particles may scatter or block light, affecting water clarity.
    * https://dec.alaska.gov/media/11018/attachment-f-faq-turbidity-in-surface-waters-110813.pdf 
```{r}
class(g3$Turbidity) #numeric
sum(is.na(g3$Turbidity)) #37716 NA values
sum(is.na(g3$Turbidity))/length(g3$Turbidity) #63.28% NA values
summary(g3$Turbidity) #Min: -0.25 Max: 3065
sum(g3$Turbidity>1000,na.rm=T)
sum(g3$Turbidity<0,na.rm=T)
```
* Data type: factor
* NA values: 37716
* Percentage NA values: 63.28%
* Range: -0.25 to 3065
* Values outside typical range: 
* Implausible values
  * Less than 0: 1 value
  * Greater than 1000: 5
* Only integers?: no, 2 decimal places

# Compare Turbidity and Settleable Solids
```{r}
ggplot(g3, aes(x=Turbidity,y=SettleableSolids)) + geom_point()
```

# Chloride
Background:
* Concentration: mg/L
* Typical Ranges:
  * Unpolluted water ranges: below 10 mg/L, sometimes below 1 mg/L
  * Typical river ranges: 11-42 mg/L
  * Seawater contaminated water sources: 5-460 mg/L
https://www.who.int/water_sanitation_health/dwq/chloride.pdf 
* Description:
  * ion commonly found in salts like NaCl, KCl, and CaCl2
```{r}
class(g3$Chloride)
summary(g3$Chloride)
length(g3$Chloride)-sum(is.na(g3$Chloride))
```
* Data type: numeric
* NA values: 59594
* Number of input values: 4
* Range: 0 to 35
* Values outside typical range: None
* Implausible values
  * The range of chloride concentrations seem to be relatively reasonable across quartiles.
* Only integers?: no, 2 decimal places

# Hardness
Background:
  * Concentration: mg/L
  * Typical Ranges:
    * soft: 0- 60 mg/L  
    * moderately hard: 61- 120 mg/L
    * hard: 121-180 mg/L
    * very hard: >180 mg/L 
    * https://www.usgs.gov/special-topics/water-science-school/science/hardness-water#:~:text=Measures%20of%20water%20hardness&text=General%20guidelines%20for%20classification%20of,Some%20content%20may%20have%20restrictions. 
  * Description:
    * Water Hardness: soap consuming capacity of water. Generally, the concentration of calcium and magnesium ions in the water
```{r}
class(g3$Hardness)
sum(is.na(g3$Hardness))
length(g3$Hardness)-sum(is.na(g3$Hardness)) 
summary(g3$Hardness)
length(g3$Hardness)-sum(is.na(g3$Hardness))
```
* Data type: numeric
* NA values: 59594
* Number of input values: 3
* Range: 42-45
* Values outside typical range: None
* Implausible values: None
* Only integers?: no, 2 decimal places