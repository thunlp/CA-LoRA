import collections
import copy

PATHBASE="/mnt/sfs_turbo/hsd/plm_cache/"
PATHBASE="/home/hushengding/plm_cache/"

AllConfigs = {}

BaseConfigs = {}
BaseConfigs['beit-base-patch16-224'] = {
                ("job_name", "task_name", "eval_dataset_name", "test_dataset_name", "num_train_epochs",
                "max_source_length",
                "per_device_train_batch_size", "per_device_eval_batch_size", "warmup_steps","save_steps", "eval_steps", "num_classes"): zip(
                    ["beans"],
                    ["beans"], #"superglue-cb", "superglue-copa", "superglue-wic", "superglue-multirc", "superglue-record", "superglue-wsc.fixed", "mrpc", "cola", "sst2", "qnli", "rte",  "mnli", "qqp", "stsb"],
                    ["beans"], #"superglue-cb", "superglue-copa", "superglue-wic", "superglue-multirc", "superglue-record", "superglue-wsc.fixed", "mrpc", "cola", "sst2", "qnli", "rte",  "mnli", "qqp", "stsb"],
                    ["beans"], #"superglue-cb", "superglue-copa", "superglue-wic", "superglue-multirc", "superglue-record", "superglue-wsc.fixed", "mrpc", "cola", "sst2", "qnli", "rte", "mnli", "qqp", "stsb"],
                    [ 20],
                    [256],
                    [ 32],
                    [ 32],#,  32,  32,  32,  32,  16,  32] + [32] * 8,
                    [0], # *7 +[0] *8,
                    [200],# 100, 50, 100, 200, 200, 100, 200, 100, 200, 200, 100, 200, 200, 100],
                    [200],#, 100, 50, 100, 200, 200, 100, 200, 100, 200, 200, 100, 200, 200, 100],
                    [ 3],
                ),
                "do_train": True,
                "do_eval": True,
                "do_test": True,

                "model_name_or_path": f"{PATHBASE}beit-base-patch16-224",
                "tokenizer_name": f"{PATHBASE}beit-base-patch16-224",
                "save_total_limit": 1,
                # For glue datasets.
                "split_validation_test": True,
                "seed": 42,
                "dataset_config_name": ["en"],
                "eval_dataset_config_name": ["en"],
                "test_dataset_config_name": ["en"],
                # other configurations.
                "predict_with_generate": False,
                # To evaluate during training.
                "load_best_model_at_end": True,
                "metric_for_best_model": "average_metrics",
                "greater_is_better": True,
                "evaluation_strategy": "steps",

                "overwrite_output_dir": True,
                "push_to_hub": False,
                "push_to_delta_center": True,
                "save_strategy": "steps",
                "datasets_load_from_disk":False,
            }

AllConfigs['bitfit_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['bitfit_beit-base-patch16-224'].update({
                "delta_type": "bitfit",
                "learning_rate": 3e-4,
                "output_dir": "outputs/bitfit/beit-base-patch16-224/",
            })

AllConfigs['adapter_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['adapter_beit-base-patch16-224'].update({
                                "delta_type": "adapter",
                                "learning_rate": 3e-4,
                                "unfrozen_modules": [
                                    "deltas",
                                    "layer_norm",
                                    "final_layer_norm"
                                ],
                                "bottleneck_dim":24,
                                "output_dir": "outputs/adapter/beit-base-patch16-224/",
                            })

AllConfigs['lora_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['lora_beit-base-patch16-224'].update({
                                "delta_type": "lora",
                                "learning_rate": 3e-4,
                                "unfrozen_modules": [
                                    "deltas",
                                    "layernorm_after",
                                    "classifier"
                                ],
                                "modified_modules":[
                                    "query",
                                    "value",
                                ],
                                "lora_r": 8,
                                "output_dir": "outputs/lora/beit-base-patch16-224/",
                            })

AllConfigs['compacter_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['compacter_beit-base-patch16-224'].update({
                                "delta_type": "compacter",
                                "learning_rate": 3e-3,
                                "unfrozen_modules": [
                                    "deltas",
                                    "layer_norm",
                                    "final_layer_norm"
                                ],
                                "output_dir": "outputs/compacter/beit-base-patch16-224/",
                                "non_linearity": "gelu_new",

                                #Compacter.
                                "hypercomplex_division": 4,
                                "hypercomplex_adapters": True,
                                "hypercomplex_nonlinearity": "glorot-uniform",
                                # gradient clip and clamp
                                "gradient_clip": False,
                                "phm_clamp": False,
                                "normalize_phm_weight": False,
                                "learn_phm": True,
                                # shared one side
                                "factorized_phm": True,
                                "shared_phm_rule": False,
                                "factorized_phm_rule": False,
                                "phm_c_init": "normal",
                                "phm_init_range": 0.0001,
                                "use_bias_down_sampler": True,
                                "use_bias_up_sampler": True,
                            })

AllConfigs['compacter++_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['compacter++_beit-base-patch16-224'].update({
                                "delta_type": "compacter",
                                "learning_rate": 3e-3,
                                "do_train": True,
                                "do_eval": True,
                                "do_test": True,
                                "modified_modules": [
                                    "DenseReluDense"
                                ],
                                "unfrozen_modules": [
                                    "deltas",
                                    "layer_norm",
                                    "final_layer_norm"
                                ],
                                "output_dir": "outputs/compacter++/beit-base-patch16-224/",
                                "non_linearity": "gelu_new",

                                #Compacter.
                                "hypercomplex_division": 4,
                                "hypercomplex_adapters": True,
                                "hypercomplex_nonlinearity": "glorot-uniform",
                                # gradient clip and clamp
                                "gradient_clip": False,
                                "phm_clamp": False,
                                "normalize_phm_weight": False,
                                "learn_phm": True,
                                # shared one side
                                "factorized_phm": True,
                                "shared_phm_rule": False,
                                "factorized_phm_rule": False,
                                "phm_c_init": "normal",
                                "phm_init_range": 0.0001,
                                "use_bias_down_sampler": True,
                                "use_bias_up_sampler": True,
                            })


AllConfigs['low_rank_adapter_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['low_rank_adapter_beit-base-patch16-224'].update({
                                "delta_type": "low_rank_adapter",
                                "learning_rate": 3e-4,
                                "unfrozen_modules": [
                                    "deltas",
                                    "layer_norm",
                                    "final_layer_norm"
                                ],
                                "output_dir": "outputs/low_rank_adapter/beit-base-patch16-224/",
                                "non_linearity": "gelu_new",
                                "low_rank_w_init": "glorot-uniform",
                                "low_rank_rank": 1,
                            })


AllConfigs['soft_prompt_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['soft_prompt_beit-base-patch16-224'].update({
                                "delta_type": "soft_prompt",
                                "learning_rate": 3e-2,
                                "soft_token_num":100,
                                "token_init": False,
                                "unfrozen_modules": [
                                    "deltas",
                                ],
                                "output_dir": "outputs/soft_prompt/beit-base-patch16-224/",
                            })

AllConfigs['prefix_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['prefix_beit-base-patch16-224'].update({
                                "delta_type": "prefix",
                                "learning_rate": 3e-4,
                                "unfrozen_modules": [
                                    "deltas",
                                ],
                                "output_dir": "outputs/prefix/beit-base-patch16-224/",
                            })

AllConfigs['soft_prompt_beit-base-patch16-224'] = copy.deepcopy(BaseConfigs['beit-base-patch16-224'])
AllConfigs['soft_prompt_beit-base-patch16-224'].update({
                                "delta_type": "soft_prompt",
                                "learning_rate": 3e-4,
                                "unfrozen_modules": [
                                    "deltas",
                                ],
                                "output_dir": "outputs/soft_prompt/beit-base-patch16-224/",
                            })



if __name__ == "__main__":
    import argparse
    import json
    import os
    parser = argparse.ArgumentParser("Parser to generate configuration")
    parser.add_argument("--job", type=str)
    args = parser.parse_args()

    config = AllConfigs[args.job]

    Cartesian_product = []
    for key in config:
        if isinstance(key, tuple):
            Cartesian_product.append(key)
    all_config_jsons = {}
    for key_tuple in Cartesian_product:
        for zipped in config[key_tuple]:
            job_name = zipped[0]
            all_config_jsons[job_name] = {}
            for key_name, zipped_elem in zip(key_tuple, zipped):
                if key_name != 'job_name':
                    all_config_jsons[job_name][key_name] = zipped_elem
    for key in config:
        if not isinstance(key, tuple):
            for job_name in all_config_jsons:
                if key == "output_dir":
                    all_config_jsons[job_name][key] = config[key] + job_name
                else:
                    all_config_jsons[job_name][key] = config[key]


    if not os.path.exists(f"configs/{args.job}/"):
        os.mkdir(f"configs/{args.job}/")

    for job_name in all_config_jsons:
        with open(f"configs/{args.job}/{job_name}.json", 'w') as fout:
            json.dump(all_config_jsons[job_name], fout, indent=4,sort_keys=True)



