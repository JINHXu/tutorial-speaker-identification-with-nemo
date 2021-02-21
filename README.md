# Speaker recognition/identification experiment with [NeMo](https://github.com/NVIDIA/NeMo)
*This is merely an experiment, the speaker inference step was not explicitly explained in the main branch in NeMo repo.*<br>
(A speaker recognition experiment with NeMo: train a speaker recognition model and perform speaker inference on test data.)<br>
This experiment is about recognizing my own voice.
```
jos-MacBook-Pro:NeMo xujinghua$ python /Users/xujinghua/NeMo/scripts/scp_to_manifest.py --scp /Users/xujinghua/NeMo/data/an4/wav/an4_clstk/train_all_75.scp --id -2 --out /Users/xujinghua/NeMo/data/an4/wav/an4_clstk/all_manifest_74.json --split
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 961/961 [00:00<00:00, 1709.86it/s]
jos-MacBook-Pro:NeMo xujinghua$ find /Users/xujinghua/test_jxu -iname "*.wav" > test_jxu.scpjos-MacBook-Pro:NeMo xujinghua$ find /Users/xujinghua/test_jxu -iname "*.wav" > /Users/xujinghua/test_jxu.scp
jos-MacBook-Pro:NeMo xujinghua$ python /Users/xujinghua/NeMo/scripts/scp_to_manifest.py --scp /Users/xujinghua/test_jxu.scp --id -2 --out /Users/xujinghua/test_jxu.json
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████| 6/6 [00:00<00:00, 724.72it/s]
jos-MacBook-Pro:NeMo xujinghua$ 
```

```
python /Users/xujinghua/speaker-reco/scripts/speaker_reco_infer.py --spkr_model /Users/xujinghua/speaker-reco/nemo_experiments/SpeakerNet/spkr.nemo --train_manifest /Users/xujinghua/speaker-reco/data/train.json --test_manifest /Users/xujinghua/speaker-reco/data/dev.json --batch_size 32
```

```
python /Users/xujinghua/speaker-reco/scripts/speaker_reco_infer.py --spkr_model /Users/xujinghua/speaker-reco/nemo_experiments/SpeakerNet/spkr.nemo --train_manifest /Users/xujinghua/speaker-reco/data/train.json --test_manifest /Users/xujinghua/speaker-reco/data/test_jxu.json --batch_size 32
```