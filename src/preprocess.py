import os
import lxml.etree as ET

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

def convert(size, box):
  dw = 1./(size[0])
  dh = 1./(size[1])
  x = (box[0] + box[1])/2.0 - 1
  y = (box[2] + box[3])/2.0 - 1
  w = box[1] - box[0]
  h = box[3] - box[2]
  x = x*dw
  w = w*dw
  y = y*dh
  h = h*dh
  return (x,y,w,h)

def convert_annotation(year, image_id):
    in_file = open('data/VOC%s/Annotations/%s.xml'%(year, image_id))
    out_file = open('data/VOC%s/labels/%s.txt'%(year, image_id), 'w')
    
    root = ET.parse(in_file).getroot()
    w = int(root.find('size').find('width').text)
    h = int(root.find('size').find('height').text)

    for obj in root.iter('object'):
        difficult = int(obj.find('difficult').text) == 1
        cls = obj.find('name').text
        if cls not in classes or difficult:
          continue
        
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

for year, image_set in sets:
    if not os.path.exists(f'data/VOC{year}/labels/'):
        os.makedirs(f'data/VOC{year}/labels/')
    image_ids = open(f'data/VOC{year}/ImageSets/Main/{image_set}.txt').read().strip().split()
    list_file = open(f'data/{year}_{image_set}.txt', 'w')
    for image_id in image_ids:
        try:
          convert_annotation(year, image_id)
          list_file.write(f'data/VOC{year}/JPEGImages/{image_id}.jpg\n')
        except:
          print(f"Missing XML {year} {image_id}")
    list_file.close()