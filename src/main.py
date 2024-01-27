import torch
from transformers import LayoutLMv3FeatureExtractor, LayoutLMv3TokenizerFast, LayoutLMv3Processor, LayoutLMv3ForTokenClassification
from trainer import *
from loader import *
from torch.optim import AdamW
import numpy as np
from engine import *

feature_extractor = LayoutLMv3FeatureExtractor(apply_ocr=False)
tokenizer = LayoutLMv3TokenizerFast.from_pretrained("microsoft/layoutlmv3-base")

processor = LayoutLMv3Processor(tokenizer=tokenizer,feature_extractor=feature_extractor)
model = LayoutLMv3ForTokenClassification.from_pretrained('microsoft/layoutlmv3-base')

if __name__ == "__main__":
    ds = dataSet('anno-converted.json',processor)
    dataload = torch.utils.data.DataLoader(ds,batch_size=2)
    # creating model instance
    model = ModelModule(5)
    # optimizer and loss
    optimizer = AdamW(model.parameters(),lr=5e-5)
    best_loss = np.inf
    # Training the model
    loss_list = []
    for epoch in range(30):
        # Training
        train_loss = train_fn(dataload, model, optimizer)
        # print(model.parameters)
        # break
        if train_loss < best_loss:
            torch.save(model.state_dict(), './model.bin')
            best_loss = train_loss

        if epoch % 10 == 0:
            torch.save(model.state_dict(), f'./model_{epoch}.bin')
            print('i = {}'.format(epoch))
            print(f"{epoch} with loss {train_loss}")

        print(f"{epoch} with loss {train_loss}")

        loss_list.append(train_loss)

        # evaluation
        eval_loss = eval_fn(dataload, model)
        print("Evaluation loss :",  eval_loss)

    np.array(loss_list).dump(open('loss_list.npy', 'wb'))