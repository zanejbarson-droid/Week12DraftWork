from earsketch import *

setTempo(115) #sets tempo for whole song

loopsClip = ZANEBARSON_JAZZBASS #used "loopsClip" to define the sound
insertMedia(loopsClip, 1, 1) #insertMedia is used due to the single use nature of the sound
setEffect(6, FILTER, FILTER_FREQ, 10000, 1, 100, 9) #Fade out effect to transition to next section

loopsClip = ZANEBARSON_JAZZGUITAR
insertMedia(loopsClip, 4, 1)
insertMedia(loopsClip, 4, 5)
setEffect(4, VOLUME, GAIN, 2) #Using effect to adjust volume of sound
setEffect(4, FILTER, FILTER_FREQ, 10000, 1, 100, 9) #Fade out effect to transition to next section

loopsClip = ZANEBARSON_JAZZDRUMS
insertMedia(loopsClip, 2, 1)
setEffect(2, VOLUME, GAIN, 2) #Using effect to adjust volume of sound
setEffect(2, FILTER, FILTER_FREQ, 10000, 1, 100, 9) #Fade out effect to transition to next section

sound = ZANEBARSON_JAZZSHAKER
insertMedia(sound, 3, 1)
setEffect(3, VOLUME, GAIN, -4) #Using effect to adjust volume of sound
setEffect(3, FILTER, FILTER_FREQ, 10000, 1, 100, 9) #Fade out effect to transition to next section

loopsClip = ZANEBARSON_NEWSAX
insertMedia(loopsClip, 6, 1)
setEffect(6, VOLUME, GAIN, -10) #Using effect to adjust volume of sound
insertMedia(loopsClip, 6, 5)    #Quick switch of volume levels
setEffect(6, VOLUME, GAIN, -10) #Using effect to adjust volume of sound
setEffect(6, FILTER, FILTER_FREQ, 10000, 1, 100, 9) #Fade out effect to transition to next section

#Second sequence of Music
sound = ZANEBARSON_STUTTER
fitMedia(sound, 7, 8, 15) #fitMedia is used to use specific sectitons/duration of sound
setEffect(7, FILTER, FILTER_FREQ, 100, 8, 10000, 15)#Used setEffect to gradually increase volume in order to sync with previous section better

sound = ZANEBARSON_SECTION2SOUND2
fitMedia(sound, 8, 8, 15) #fitMedia is used to use specific sectitons/duration of sound
setEffect(8, FILTER, FILTER_FREQ, 100, 8, 10000, 15) #Used setEffect to gradually increase volume in order to sync with previous section better

sound = ZANEBARSON_SECTION2SOUND3
insertMedia(sound, 9, 16.05) #insertMedia due to it being a single use
setEffect(9, VOLUME, GAIN, 10) #Using effect to adjust volume of sound

sound = ZANEBARSON_SIMPLESNARE
slice = createAudioSlice(sound, 1, 1.05) #slice finction is used to only use specific part of the sound
insertMedia(slice, 10, 11)               #Used 'slice' in code for the specific sound
insertMedia(slice, 10, 11.2)
insertMedia(slice, 10, 11.4)
insertMedia(slice, 10, 11.6)
insertMedia(slice, 10, 11.8)
insertMedia(slice, 10, 12)
insertMedia(slice, 10, 12.2)
insertMedia(slice, 10, 12.4)
insertMedia(slice, 10, 12.6)
insertMedia(slice, 10, 12.8)
insertMedia(slice, 10, 13)
insertMedia(slice, 10, 13.2)
insertMedia(slice, 10, 13.4)
insertMedia(slice, 10, 13.6)
insertMedia(slice, 10, 13.8)
insertMedia(slice, 10, 14)                  #decrease of duration/pause between sounds
insertMedia(slice, 10, 14.1)
insertMedia(slice, 10, 14.2)
insertMedia(slice, 10, 14.3)
insertMedia(slice, 10, 14.4)
insertMedia(slice, 10, 14.5)
insertMedia(slice, 10, 14.6)
insertMedia(slice, 10, 14.7)
insertMedia(slice, 10, 14.8)
insertMedia(slice, 10, 14.9)
insertMedia(slice, 10, 15)                      #and again
insertMedia(slice, 10, 15.05)
insertMedia(slice, 10, 15.10)
insertMedia(slice, 10, 15.15)
insertMedia(slice, 10, 15.20)
insertMedia(slice, 10, 15.25)
insertMedia(slice, 10, 15.30)
insertMedia(slice, 10, 15.35)
insertMedia(slice, 10, 15.40)
insertMedia(slice, 10, 15.45)
insertMedia(slice, 10, 15.50)
insertMedia(slice, 10, 15.55)
insertMedia(slice, 10, 15.60)
insertMedia(slice, 10, 15.65)
insertMedia(slice, 10, 15.70)
insertMedia(slice, 10, 15.75)
insertMedia(slice, 10, 15.80)
insertMedia(slice, 10, 15.85)
insertMedia(slice, 10, 15.90)
insertMedia(slice, 10, 15.95)
insertMedia(slice, 10, 16)
setEffect(10, VOLUME, GAIN, -5)         #Using effect to adjust volume of sound

sound = ZANEBARSON_DROPINTRO
insertMedia(sound, 11, 16.6) #Have to use specific timing in order to sync with Music on line 9
setEffect(11, VOLUME, GAIN, 10) #Using effect to adjust volume of sound

#drop at 16.8 beat

sound = ZANEBARSON_HEAVYSYNTH
fitMedia(sound, 12, 16.8, 20.2) #Have to use specific timing in order to sync with Drop
setEffect(12, VOLUME, GAIN, -6) #Using effect to adjust volume of sound

sound = ZANEBARSON_SECTION2TEST3
insertMedia(sound, 13, 16.8)
setEffect(13, VOLUME, GAIN, 6) #Using effect to adjust volume of sound

sound = ZANEBARSON_DROHIGH2
insertMedia(sound, 14, 16.8)
insertMedia(sound, 14, 17.6)
insertMedia(sound, 14, 18.4)
insertMedia(sound, 14, 19.2)
insertMedia(sound, 14, 20)
insertMedia(sound, 14, 20.8)
setEffect(14, VOLUME, GAIN, 6) #Using effect to adjust volume of sound

sound = ZANEBARSON_DROHIGHOFF
insertMedia(sound, 15, 19.6)
insertMedia(sound, 15, 20.4)
insertMedia(sound, 15, 21.2)
setEffect(15, VOLUME, GAIN, 6) #Using effect to adjust volume of sound

sound = ZANEBARSON_SECTION2BASSLINE
fitMedia(sound, 16, 21.5, 26.15) #fitMedia is used to use specific sectitons/duration of sound
setEffect(16, VOLUME, GAIN, 8)   #Using effect to adjust volume of sound
fitMedia(sound, 22, 26.15, 30.8) #fitMedia is used to use specific sectitons/duration of sound
setEffect(22, VOLUME, GAIN, 0.5) #Using effect to adjust volume of sound

sound = ZANEBARSON_SECTION2TEST1
fitMedia(sound, 17, 17, 20.4)  #fitMedia is used to use specific sectitons/duration of sound
setEffect(17, VOLUME, GAIN, 4) #Using effect to adjust volume of sound

sound = ZANEBARSON_SECTION2TEST2
slice = createAudioSlice(sound, 1, 1.2)
insertMedia(slice, 18, 17.7)
insertMedia(slice, 18, 18)
insertMedia(slice, 18, 18.3)
insertMedia(slice, 18, 18.5)
insertMedia(slice, 18, 18.7)
insertMedia(slice, 18, 18.9)
insertMedia(slice, 18, 19.3)
insertMedia(slice, 18, 19.5)
insertMedia(slice, 18, 19.7)
insertMedia(slice, 18, 19.9)
insertMedia(slice, 18, 20.3)
insertMedia(slice, 18, 20.5)
insertMedia(slice, 18, 20.7)
insertMedia(slice, 18, 20.9)
setEffect(18, VOLUME, GAIN, 2)  #Using effect to adjust volume of sound

sound = ZANEBARSON_SECTION2BASSLINE2
slice = createAudioSlice(sound, 1, 2.33)
insertMedia(slice, 19, 26.15)
insertMedia(slice, 23, 27.48)
insertMedia(slice, 23, 28.81)
fitMedia(slice, 19, 29.14, 29.77)   #fitMedia is used to use specific sectitons/duration of sound
setEffect(19, VOLUME, GAIN, 5)  #Using effect to adjust volume of sound
setEffect(23, VOLUME, GAIN, 8)  #Different lines are used in order to use different sound levels without changing it after every use

sound = ZANEBARSON_SECTION2TESTREVIVE
insertMedia(sound, 20, 19.3)
setEffect(20, VOLUME, GAIN, 10)  #Using effect to adjust volume of sound

sound = ZANEBARSON_SECTION2BASSLINE2
slice = createAudioSlice(sound, 1.5, 1.8)
insertMedia(slice, 21, 26.15)
insertMedia(slice, 21, 26.81)
insertMedia(slice, 21, 27.48)
insertMedia(slice, 21, 28.18)
insertMedia(slice, 21, 28.81)
setEffect(21, VOLUME, GAIN, 10) #Using effect to adjust volume of sound

sound = ZANEBARSON_VOCALTEST1
insertMedia(sound, 24, 21.5)
setEffect(24, VOLUME, GAIN, -6) #Using effect to adjust volume of sound
slice = createAudioSlice(sound, 1, 1.2)
insertMedia(slice, 25, 26.15)
insertMedia(slice, 25, 26.35)
insertMedia(slice, 25, 26.75)
insertMedia(slice, 25, 26.95)
insertMedia(slice, 25, 27.35)
insertMedia(slice, 25, 27.55)
insertMedia(slice, 25, 27.95)
insertMedia(slice, 25, 28.15)
insertMedia(slice, 25, 28.55)
insertMedia(slice, 25, 28.75)
insertMedia(slice, 25, 29.15)
insertMedia(slice, 25, 29.35)
insertMedia(slice, 25, 29.75)
insertMedia(slice, 25, 30.05)
setEffect(25, VOLUME, GAIN, 4) #Using effect to adjust volume of sound

sound = ZANEBARSON_VOCALTEST2
insertMedia(sound, 26, 21.5)
insertMedia(sound, 27, 26.15)
setEffect(26, VOLUME, GAIN, -8) #Using effect to adjust volume of sound
setEffect(27, VOLUME, GAIN, 5)  #Different lines are used in order to use different sound levels without changing it after every use

sound = ZANEBARSON_808TEST1
fitMedia(sound, 28, 21.5, 26.15)  #fitMedia is used to use specific sectitons/duration of sound
fitMedia(sound, 28, 26.15, 30.8)  #fitMedia is used to use specific sectitons/duration of sound
