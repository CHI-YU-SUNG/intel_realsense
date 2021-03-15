import cv2

cap = cv2.VideoCapture(0)
cap.set(3,320)#寬
cap.set(4,240)#高
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 為儲存視訊做準備
fourcc = cv2.VideoWriter_fourcc(*'mpeg')
fps=25
out = cv2.VideoWriter('output2.avi', fourcc,fps,sz)
while True:
    # 一幀一幀的獲取影象
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        # 在幀上進行操作
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 開始儲存視訊
        out.write(frame)
        # 顯示結果幀
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 釋放攝像頭資源
cap.release()
out.release()
cv2.destroyAllWindows()
