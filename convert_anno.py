import json

def convert_bounding_box(x, y, width, height):
    x1 = x
    y1 = y
    x2 = x + width
    y2 = y + height
    return [x1, y1, x2, y2]

with open("dataset/label_studio_anno-ohe.json") as f:
    data = json.load(f)

output = []

for annoatated_image in data:
    data = {}
    annotation = []
    ann_list = []

    if len(annoatated_image) < 8:
        continue
    for k, v in annoatated_image.items():
        if k == 'ocr':
            v = v.split('8080/')[-1]
            print(f'filename: {v}')
            data["file_name"] = f"dataset/{v}"
            output.append(data)
        if k == 'bbox':
            width = v[0]['original_width']
            height = v[0]['original_height']
            data["height"] = height
            data["width"] = width

    for bb, text, label in zip(annoatated_image['bbox'], annoatated_image['transcription'],   annoatated_image['label']):
        ann_dict = {}
        print('text :', text)
        ann_dict["box"] = convert_bounding_box(bb['x'], bb['y'], bb['width'], bb['height'])
        ann_dict["text"] = text
        ann_dict["label"] = label['labels'][-1]
        ann_list.append(ann_dict)
    data["annotations"] = ann_list

print(output)
with open("Training_layoutLMV3.json", "w") as f:
  json.dump(output, f, indent=4)
