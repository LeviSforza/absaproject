# -*- coding: utf-8 -*-
# file: __init__.py
# time: 02/11/2022 15:47
# author: YANG, HENG <hy345@exeter.ac.uk> (杨恒)
# github: https://github.com/yangheng95
# GScholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# ResearchGate: https://www.researchgate.net/profile/Heng-Yang-17/research
# Copyright (C) 2022. All Rights Reserved.


class GloVeRNARModelList(list):
    from .classic.cnn import CNN
    from .classic.lstm import LSTM
    from .classic.transformer import Transformer
    from .classic.mhsa import MHSA

    CNN = CNN
    LSTM = LSTM
    Transformer = Transformer
    MHSA = MHSA

    def __init__(self):
        super(GloVeRNARModelList, self).__init__(
            [self.CNN, self.LSTM, self.Transformer, self.MHSA]
        )


class BERTRNARModelList(list):
    from .plm.bert import BERT_MLP

    BERT_MLP = BERT_MLP

    def __init__(self):
        super(BERTRNARModelList, self).__init__([self.BERT_MLP])
