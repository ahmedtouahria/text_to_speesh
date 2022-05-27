from io import BytesIO
import tempfile
from django.core.files import File
from django.db import models
from gtts.tts import gTTS
# Create your models here.
class Text(models.Model):
    LANG=[("ar","ar"),("fr","fr")]
    contenu=models.CharField(max_length=600)
    audio = models.FileField(upload_to="media/audio",blank=True, null=True)
    lang=models.CharField( max_length=50,choices=LANG,default="ar")
    normalization=models.CharField(max_length=600,blank=True, null=True)
    
    def __str__(self):
        return self.contenu[:15]
    def save(self, *args, **kwargs):
        new_string =str(self.normalization)
        file_name = '{}.mp3'.format(str(self.normalization).lower().replace(' ', '_'))
        make_sound = gTTS(text=new_string, lang=self.lang)
        mp3_fp = BytesIO()
        make_sound.write_to_fp(mp3_fp)
        self.audio.save(file_name, mp3_fp, save=False)
        super(Text, self).save(*args, **kwargs)
