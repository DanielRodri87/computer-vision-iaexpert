import CVz

2

video = cv2. VideoCapture("street.mp4")

rastreador = cv2. TrackerCSRT_create()

ok, frame = video.read()

11
12
13

15
16

18
19

bbox = cv2. selectROI(frame)

ok = rastreador.init(frame, bbox)

while True:
ok, frame = video.read()
#print(ok)
if not ok:
break

22

24
25
26

28
29

ok, bbox = rastreador. update(frame)
#print(bbox)

if ok:
(x, y, w, h) = [int(v) for v in bbox]
cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
else:
cv2.putText(frame, 'Erro', (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow('Rastreamento', frame)

if cv2.waitKey(1) & OXFF == 27: