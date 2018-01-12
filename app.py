from flask import Flask, render_template, request
import random
import os
import time;
app = Flask(__name__)

outFileName = './result.txt';
wavPath = './static/music/'
samples = ['s1','s2','s3','s4'] # The directory names
inds = [0,1,2,3] # Making the randomized indices global
files = [] # 2D array containing all the wav files in the sample directories
for i in range(0,len(samples)):
    files.append([f for f in os.listdir(wavPath+samples[i]) if f.endswith(".wav")])


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/page2",methods = ['POST'])
def page2():
    name = request.form['NAME']
    mailID = request.form['MAIL']
    localtime = time.asctime(time.localtime(time.time()))
    outFile = open(outFileName,"w");
    outFile.write("Name: "+name+"\nEmail: "+mailID+"\nTimestamp: "+localtime+"\n")
    outFile.close()
    random.shuffle(inds)
    #print(files[0][inds[0]],files[0][inds[1]],files[0][inds[2]],files[0][inds[3]]+" \n")
    return render_template('page2.html',music_files=files[0][inds[0]],music_files2=files[0][inds[1]],music_files3=files[0][inds[2]],music_files4=files[0][inds[3]],music_files_number=4)

@app.route("/page3",methods = ['POST'])
def page3():
    a = request.form['optradio1']
    b = request.form['optradio2']
    c = request.form['optradio3']
    d = request.form['optradio4']
    outFile = open(outFileName,"a");
    print(a,b,c,d)
    outFile.write(files[0][inds[0]]+" "+a+"\n")
    outFile.write(files[0][inds[1]]+" "+b+"\n")
    outFile.write(files[0][inds[2]]+" "+c+"\n")
    outFile.write(files[0][inds[3]]+" "+d+"\n")
    outFile.close()
    return render_template('finished.html')

if __name__ == "__main__":
    app.run()
