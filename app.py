from pydub import AudioSegment
import csv,sys

def process_file(c):
    with open('csvs/'+c[0].replace('asf','csv'),'w') as csvfile:
        writer = csv.writer(csvfile)
        start = float(c[1])
        audio = AudioSegment.from_file('chunks/'+c[0])
        points = [['x','y']]
        for i in range(0,len(audio),1000):
            points.append([audio[i:i+1000].dBFS,start+i])
        
        writer.writerows(points)
    csvfile.close()



if __name__ == "__main__":
    with open(sys.argv[1],'r') as file:
        reader = csv.reader(file)
        for row in reader:
            process_file(row)
            print("wrote {}".format(row[0]))
