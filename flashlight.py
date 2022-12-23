//Este código foi desenvolvido em um tutorial do Youtube para ativar a lâmpada do celular de acordo com uma confirmação na tela por parte do usuário
//o programa foi desenvolvido em Python para Android

import android
import os

droid = android.Android()
def cls():
  os.system(['clear','cls'][os.name == 'nt'])
  def turnon():
    light = open('/sys/classe/leds/torch=flash/flash_light', 'w')
    light.write('1')
    
    def turnoff():
    light = open('/sys/classe/leds/torch=flash/flash_light', 'w')
    light.write('0')   
    
    title = 'Flashlight Toggle'
    message = 'By. Quitarman2020'
    doid.dialogCreateAlert(title.message)
    doird.dialogSetPositiveButtonText('Ok')
    doid.dialogShow()
    response = doid.dialogGetResponse().result
    yep = response['which'] == 'positive'
    
    title = 'Flashlight Toggle'
    droid.dialogCreateAlert(title)
    droid.dialogSetPositiveButtonText('Shine')
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    light = response['which'] == 'positive'
    
    if light:
      turnon()
   
  cls()
  title = 'Turn off'
  droid.dialogCreateAlert(title)
  droid.dialogShow()
  response = droid.dialogGetResponse().result
  dark = response['which'] == 'positive'
  
  if dark:
    turnoff()
    
 cls()
  
      
