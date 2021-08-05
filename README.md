# TUTORIAL: Speaker Identification with `Nemo` 

A comprehensible and quick illustration on how to do speaker identification on your own data with NVIDIA's `Nemo`

1. record data
2. data prep
3. config
4. fine tune
5. inference
6. evaluation

## Record your own data of speakers intended to be identified

* preprocess into intended format
* slice into around 4 seconds audio samples

_Recommended tool `pydub`_

##  Data Prep (generate train, dev, test manifests)

* [instructions](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_recognition/datasets.html)

## Configration

* change from [default config](https://github.com/JINHXu/NeMo/blob/main/examples/speaker_recognition/conf/SpeakerNet_recognition_3x2x512.yaml)
* [documentations & instructions](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/speaker_recognition/configs.html#)


## Fine-tune `SpeakerNet` on data of speakers intended to be identified

* [pre-trained model](https://ngc.nvidia.com/catalog/models/nvidia:nemo:speakerrecognition_speakernet)

* fine tune [script](https://github.com/NVIDIA/NeMo/blob/main/examples/speaker_recognition/speaker_reco_finetune.py)
 

## Inference

* inference [script](https://github.com/NVIDIA/NeMo/blob/main/examples/speaker_recognition/speaker_reco_infer.py)


## (Evaluation)

* [eva](https://github.com/JINHXu/speaker-reco/blob/main/scripts/evaluation.py)
