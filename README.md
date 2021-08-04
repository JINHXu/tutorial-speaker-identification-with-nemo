# Speaker Identification with `Nemo` tutorial

1. Data Prep (generate train, dev, test manifests)

* [instructions](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_recognition/datasets.html)

2. Configration

* change from [default config](https://github.com/JINHXu/NeMo/blob/main/examples/speaker_recognition/conf/SpeakerNet_recognition_3x2x512.yaml)
* [documentations & instruction](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_recognition/configs.html#)


3. Fine-tune `SpeakerNet`

* [script](https://github.com/NVIDIA/NeMo/blob/main/examples/speaker_recognition/speaker_reco_finetune.py)
 

4. Inference

* [inference](https://github.com/NVIDIA/NeMo/blob/main/examples/speaker_recognition/speaker_reco_infer.py)


(5. Evaluation)

* [eva](https://github.com/JINHXu/speaker-reco/blob/main/scripts/evaluation.py)
