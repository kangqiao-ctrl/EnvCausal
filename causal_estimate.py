import dowhy
import econml

def causal_estimate(treatment,data,outcome,causal_graph)
    f = open(treatment+outcome+".txt", "w+")
    f.close()

    inspect_datasets = True
    inspect_models = True
    inspect_identified_estimands = True
    inspect_estimates = True
    inspect_refutations = True

    dowhy.causal_refuter.CausalRefuter.DEFAULT_NUM_SIMULATIONS = 100

    dataset = data

    causal_graph = causal_graph

    model = dowhy.CausalModel(data = dataset,
                        treatment = treatment,
                        outcome = outcome,
                        graph = causal_graph.replace("\n", " "))
                        

    if inspect_models is True:
        with open(treatment+outcome+".txt", "a") as f:
            print("####### Model #############################################################################################",file=f)
            print("Dataset Identifier:",(min(model._data['elapsed']),max(model._data['elapsed'])),file=f)
            print("Common Causes:",model._common_causes,file=f)
            print("Effect Modifiers:",model._effect_modifiers,file=f)
            print("Instruments:",model._instruments,file=f)
            print("Outcome:",model._outcome,file=f)
            print("Treatment:",model._treatment,file=f)
            print("#############################################################################################################",file=f)

    estimand = model.identify_effect(proceed_when_unidentifiable=True)

    with open(treatment+outcome+".txt", "a") as f:
        print("####### Identified Estimand #####################################################################################",file=f)
        print(estimand,file=f)
        print("###################################################################################################################",file=f)

    estimate_li = model.estimate_effect(estimand,method_name = "backdoor.linear_regression", method_params = None)
    estimate_forest = model.estimate_effect(estimand,method_name ="backdoor.econml.ortho_forest.ContinuousTreatmentOrthoForest",method_params = {"init_params":{"n_jobs":32},"fit_params":{}})
        
    if inspect_estimates is True:
        with open(treatment+outcome+".txt", "a") as f:
            #Linear Results
            print("####### Linear Estimate ################################################################################",file=f)
            print("*** Class Name ***",file=f)
            print(estimate_li.params['estimator_class'],file=f)
            print("*** Treatment Name ***",file=f)
            print(min(model._data['elapsed']),max(model._data['elapsed']),file=f)
            print(model._treatment,file=f)
            print(estimate_li,file=f)
            print("########################################################################################################",file=f)
            #Forest Results
            print("####### Forest Estimate#################################################################################",file=f)
            print("*** Class Name ***",file=f)
            print(estimate_forest.params['estimator_class'],file=f)
            print("*** Treatment Name ***",file=f)
            print(min(model._data['elapsed']),max(model._data['elapsed']),file=f)
            print(model._treatment,file=f)
            print(estimate_forest,file=f)
            print("########################################################################################################",file=f)
                   
    refutation_li_ptr = model.refute_estimate(estimand,estimate_li,method_name='placebo_treatment_refuter')
    refutation_forest_ptr = model.refute_estimate(estimand,estimate_forest,method_name='placebo_treatment_refuter')

    if inspect_refutations is True:
        with open(treatment+outcome+".txt", "a") as f:
            # Linear PTR Refute Result
            print("####### Linear PTR Refutation #######################################################################################",file=f)
            print("*** Class Name ***",file=f)
            print(refutation_li_ptr.refutation_type,file=f)
            print(refutation_li_ptr,file=f)        
            print("########################################################################################################",file=f)
            # Forest PTR Refute Result
            print("####### Forest PTR Refutation#######################################################################################",file=f)
            print("*** Class Name ***",file=f)
            print(refutation_forest_ptr.refutation_type,file=f)
            print(refutation_forest_ptr,file=f)        
            print("########################################################################################################",file=f)

    refutation_li_rcc = model.refute_estimate(estimand,estimate_li,method_name='random_common_cause')
    refutation_forest_rcc = model.refute_estimate(estimand,estimate_forest,method_name='random_common_cause')

    if inspect_refutations is True:
        with open(treatment+outcome+".txt".txt", "a") as f:
            # Linear RCC Refute Result
            print("####### Linear RCC Refutation #######################################################################################",file=f)
            print("*** Class Name ***",file=f)
            print(refutation_li_rcc.refutation_type,file=f)
            print(refutation_li_rcc,file=f)        
            print("########################################################################################################",file=f)
            # Forest RCC Refute Result
            print("####### Forest RCC Refutation#######################################################################################",file=f)
            print("*** Class Name ***",file=f)
            print(refutation_forest_rcc.refutation_type,file=f)
            print(refutation_forest_rcc,file=f)        
            print("########################################################################################################",file=f)