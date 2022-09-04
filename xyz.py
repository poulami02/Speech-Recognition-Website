from flask import Flask, render_template, request, redirect, url_for, send_file
import moviepy.editor
import os
import sys
from moviepy.editor import VideoFileClip
from werkzeug.utils import secure_filename

import speech_recognition as sr
from deep_translator import GoogleTranslator

app=Flask(__name__,template_folder='template')

@app.route('/', methods=['GET','POST'])
def audio():
	if request.method=="POST":
		if "file" not in request.files:
			return redirect(request.url)

		file=request.files["file"]
		if file.filename=="":
			return redirect(request.url)

		if file:
			filename, ext = os.path.splitext(file.filename)
			clip = VideoFileClip("C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/"f"{file.filename}")
			audio=clip.audio
			audio.write_audiofile("C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/"f"P.wav")
			path_to_file = "C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/"f"P.wav"

			return send_file(
                path_to_file, 
                mimetype="audio/wav", 
                as_attachment=True, 
                attachment_filename="Audio.wav")

		
			
	return render_template('xyz.html')

@app.route('/english', methods=['GET','POST'])
def english():
	transcript=""

	path_to_file0 = "C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/"f"P.wav"

	recognizer=sr.Recognizer()
	with sr.AudioFile(path_to_file0) as source:
		data=recognizer.record(source)
		transcript=recognizer.recognize_google(data, key=None)

	return render_template('english.html', transcript=transcript)


@app.route('/bengali', methods=['GET','POST'])
def bengali():
	path_to_file1 = "C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/P.wav"
	recognizer1=sr.Recognizer()
	with sr.AudioFile(path_to_file1) as source:
		data1=recognizer1.record(source)
		transcript1=recognizer1.recognize_google(data1, key=None)
		translated=GoogleTranslator(source='auto', target='bn').translate(transcript1)

	return render_template('bengali.html', translated=translated)
	

@app.route('/hindi', methods=['GET','POST'])
def hindi():
	path_to_file2 = "C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/P.wav"
	recognizer2=sr.Recognizer()
	with sr.AudioFile(path_to_file2) as source:
		data2=recognizer2.record(source)
		transcript2=recognizer2.recognize_google(data2, key=None)
		translated1=GoogleTranslator(source='auto', target='hi').translate(transcript2)

	return render_template('hindi.html', translated1=translated1)

@app.route('/spanish', methods=['GET','POST'])
def spanish():
	path_to_file3 = "C:/Users/User/AppData/Roaming/Python/Python310/Scripts/Speech Recognition/template/Videos/P.wav"
	recognizer3=sr.Recognizer()
	with sr.AudioFile(path_to_file3) as source:
		data3=recognizer3.record(source)
		transcript3=recognizer3.recognize_google(data3, key=None)
		translated2=GoogleTranslator(source='auto', target='es').translate(transcript3)

	return render_template('spanish.html', translated2=translated2)
	
if __name__=='__main__':
	app.run(debug=True, threaded=True)