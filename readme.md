# Supervised machine learning project
---
## Classification of PM2.5 concentration using machine learning approach 
### Google Colab link is [here](https://colab.research.google.com/drive/1__UHk7F9gGWpOvjv1G5mj6nBv-XVNn9Q?usp=sharing)
**[Here](https://air-quality-dash-app.ew.r.appspot.com) is the data visualization dashboard app created in [DASH](https://plotly.com/dash/)<br>**
**and deployed using GCP App engine**  

In this project, we tested 5 different machine learning classification models to find out the best performing model for classifying PM 2.5 concentration levels. 

Particulate matters or PM are non gaseous compounds and elements that can be found suspended in the air. Some of the PMs are toxix and hazardous. PM10 and PM2.5 refer to the particulate matter smaller than 10 and 2.5 microns in diameters respectively. High concentration or long term exposure of these toxic elements is a major public health concern.
<br>
<br>
<img src="https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/slide03.jpg" alt="Your image title" width="250"/>


![alt text-1](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/slide03.jpg)


Exposure to PMs was found to be associated with serios health condition including cardiovascular disease, respiratory symptoms, diabetes, morbidity, mortatilty and others. In 2008, it is estimated that the average reduction in life expectancy of UK residents as a result of long term exposure to PM2.5 is months. In that year alone, it was estimated that 29,000 people lost their lives early due to PM2.5 exposure 1. In the following year, 7% of total death in UK was associated air pollution. 

![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide04.jpg) ![alt-text-3](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide06.jpg)

![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/annual_uk-pm-concentration.jpg)


Only cardiovascular disease cost the UK economy £29.1 billion in 2004. 60% of this cost was accounted to health 2. Due to significantly adverse public health threat that PM2.5 poses it is going to be benificial for people to have access to an automatic prediction system that will alert if the PM2.5 concentration is above a certain level. Current PM2.5 air quality banding system and proposed classification is discussed in the following paragraphs.

**UK Air quality banding**
<br>
According to Committee on the Medical Effects of Air Pollutants (COMEAP) the overall air pollution index for a site or region is determined by the highest concentration of five pollutants:

- Nitrogen Dioxide
- Sulphur Dioxide
- Ozone
- Particles smaller than 2.5µm (PM2.5)
- Particles smaller than  10µm (PM10)

Air quality index scale is a scale between 1-10, which is further divided in four categories: low, medium, high and very high.

The concentration range for PM2.5 is given in the following image. The concetration range for other pollutants can be found on defra's [site](https://uk-air.defra.gov.uk/air-pollution/daqi?view=more-info&pollutant=pm25#pollutant)
<br>
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/pm25-concentration-banding.jpg)
Source: uk-air.defra.gov.uk
<br>
**Classification of PM2.5 concentration**
<br>
According to World Health Organization, the  guideline values for fine particulate matter (PM2.5) are: 
- Annual mean < 10 μg/m3 
- 24-hour mean < 25 μg/m3 

To simplify our model, we considered that if PM2.5 concentration is less than 10 then it will be defined as class 1,otherwise it will be defined as class 0

It is to be noted that this station measures Urban Background data at an altitude of 5m. Therefore, pollutant concentration level by the roadside [3] and low altitude level (average height level) is expected to be much higher. This is why the prediction based on this dataset will be highly non conserative.<br>

![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide08.jpg)

![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide08.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide09.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide010.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide11.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide12.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide13.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide14.jpg)
![alt-text-2](https://github.com/szabeenglobal/Classification-of-PM2.5-concentration-using-machine-learning-approach/blob/main/images/Slide15.jpg)
