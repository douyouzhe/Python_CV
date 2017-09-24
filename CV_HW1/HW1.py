import cv2


def p2(binary_in):  # return labels_out
    shape = binary_in.shape
    a = np.zeros(shape, int); # label matrix
    k = 1
    b = []
    c = []

    for i in range(shape[0]): # 1 is white o is background
        for j in range(shape[1]):
            if binary_in[i,j] == 0: #background
                a[i,j] = 0;
            elif binary_in[i,j] == 255 and a[i-1,j-1] != 0: #D is labeled
                a[i,j] = a[i-1,j-1];
            elif binary_in[i,j] == 255 and a[i-1,j] == 0 and a[i,j-1] == 0: #B and C are not labeled
                a[i,j] = k;
                k+=1; #update label
            elif binary_in[i,j] == 255 and a[i-1,j] !=0 and a[i,j-1] ==0: #B is labeled
                a[i,j] = a[i-1,j];
            elif binary_in[i,j] == 255 and a[i,j-1] !=0 and a[i-1,j] ==0: #C is labeled
                a[i,j] = a[i,j-1];
            elif a[i,j-1] !=0 and a[i-1,j] !=0: #B and C are labeled
                if a[i,j-1] ==  a[i-1,j] :
                    a[i,j] = a[i,j-1];
                else:
                    a[i,j] = a[i,j-1];
                    b.append(a[i-1,j]);
                    c.append(a[i,j-1]);
    k=0; h=0
    b_t = np.array(b)


    for k in range(len(b)): #Create Eq_Table
        for h in range(len(c)):
            if b[h]==c[k]:
                b[h]=b[k]

    for k in range(len(c)):
        for h in range(len(c)):
            if c[h]==c[k]:
                for i in range(len(b)):
                    if b[i]==b[h]:
                        b[i]=b[k]


    for k in range(len(c)):
        for i in range(shape[0]):
            for j in range(shape[1]):
                if a[i,j] == c[k]:
                    a[i,j] = b[k]

    for k in range(len(b)):
        for i in range(shape[0]):
            for j in range(shape[1]):
                if a[i,j] == b_t[k]:
                    a[i,j] = b[k]+100

    cv2.imwrite('New_label.pgm', a, (cv2.IMWRITE_PXM_BINARY, 0));


    return a;