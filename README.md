# TUTORIAL: Speaker Identification with `Nemo` 

A tutorial on how to do speaker identification on your own data with NVIDIA's `Nemo`

0. Record your own data of speakers intended to be identified

* preprocess into intended format
* slice into around 4 seconds audio samples

_Recommended tool `pydub`_

1. Data Prep (generate train, dev, test manifests)

* [instructions](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_recognition/datasets.html)

2. Configration

* change from [default config](https://github.com/JINHXu/NeMo/blob/main/examples/speaker_recognition/conf/SpeakerNet_recognition_3x2x512.yaml)
* [documentations & instructions](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_recognition/configs.html#)


3. Fine-tune `SpeakerNet` on data of speakers intended to be identified

* [pre-trained model](https://ngc.nvidia.com/catalog/models/nvidia:nemo:speakerrecognition_speakernet)

* fine tune [script](https://github.com/NVIDIA/NeMo/blob/main/examples/speaker_recognition/speaker_reco_finetune.py)
 

4. Inference

* inference [script](https://github.com/NVIDIA/NeMo/blob/main/examples/speaker_recognition/speaker_reco_infer.py)


(5. Evaluation)

* [eva](https://github.com/JINHXu/speaker-reco/blob/main/scripts/evaluation.py)
