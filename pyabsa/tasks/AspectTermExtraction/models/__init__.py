# -*- coding: utf-8 -*-
# file: __init__.py
# time: 02/11/2022 15:47
# author: YANG, HENG <hy345@exeter.ac.uk> (杨恒)
# github: https://github.com/yangheng95
# GScholar: https://scholar.google.com/citations?user=NPq5a_0AAAAJ&hl=en
# ResearchGate: https://www.researchgate.net/profile/Heng-Yang-17/research
# Copyright (C) 2022. All Rights Reserved.


class ATEPCModelList(list):
    from .lcf.bert_base_atepc import BERT_BASE_ATEPC
    from .lcf.fast_lcf_atepc import FAST_LCF_ATEPC
    from .lcf.fast_lcfs_atepc import FAST_LCFS_ATEPC
    from .lcf.lcf_atepc import LCF_ATEPC
    from .lcf.lcf_atepc_large import LCF_ATEPC_LARGE
    from .lcf.lcf_template_atepc import LCF_TEMPLATE_ATEPC
    from .lcf.lcfs_atepc import LCFS_ATEPC
    from .lcf.lcfs_atepc_large import LCFS_ATEPC_LARGE

    BERT_BASE_ATEPC = BERT_BASE_ATEPC
    FAST_LCF_ATEPC = FAST_LCF_ATEPC
    FAST_LCFS_ATEPC = FAST_LCFS_ATEPC
    LCF_ATEPC = LCF_ATEPC
    LCF_ATEPC_LARGE = LCF_ATEPC_LARGE
    LCFS_ATEPC = LCFS_ATEPC
    LCFS_ATEPC_LARGE = LCFS_ATEPC_LARGE

    LCF_TEMPLATE_ATEPC = LCF_TEMPLATE_ATEPC

    def __init__(self):
        super(ATEPCModelList, self).__init__(
            [
                self.BERT_BASE_ATEPC,
                self.FAST_LCF_ATEPC,
                self.FAST_LCFS_ATEPC,
                self.LCF_ATEPC,
                self.LCF_ATEPC_LARGE,
                self.LCFS_ATEPC,
                self.LCFS_ATEPC_LARGE,
            ]
        )
