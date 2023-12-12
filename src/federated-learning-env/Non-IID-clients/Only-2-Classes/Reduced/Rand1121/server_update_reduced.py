import tensorflow as tf
import flwr as fl
from sys import argv
from typing import List, Tuple, Union, Dict, Optional
from flwr.server.client_proxy import ClientProxy


from flwr.common import (
    EvaluateIns,
    EvaluateRes,
    FitIns,
    FitRes,
    MetricsAggregationFn,
    NDArrays,
    Parameters,
    Scalar,
    ndarrays_to_parameters,
    parameters_to_ndarrays,
)
#from flwr import ClientProxy, EvaluateRes, FitRes
serverPort = '8080'
numRounds = 400

if len(argv) >= 2:
    serverPort = argv[1]
    
    
class AggregateCustomMetricStrategy(fl.server.strategy.FedAvg):
    def aggregate_evaluate(
        self,
        server_round: int,
        results: List[Tuple[ClientProxy, EvaluateRes]],
        failures: List[Union[Tuple[ClientProxy, FitRes], BaseException]],
    ) -> Tuple[Optional[float], Dict[str, Scalar]]:
        """Aggregate evaluation accuracy using weighted average."""

        if not results:
            return None, {}

        # Call aggregate_evaluate from base class (FedAvg) to aggregate loss and metrics
        aggregated_loss, aggregated_metrics = super().aggregate_evaluate(server_round, results, failures)

        # Weigh accuracy of each client by number of examples used
        accuracies = [r.metrics["accuracy"] * r.num_examples for _, r in results]
        examples = [r.num_examples for _, r in results]

        # Aggregate and print custom metric
        aggregated_accuracy = sum(accuracies) / sum(examples)
        print(f"Round {server_round} accuracy aggregated from client results: {aggregated_accuracy}")

        # Return aggregated loss and metrics (i.e., aggregated accuracy)
        return aggregated_loss, {"accuracy": aggregated_accuracy}

# Create strategy and run server
strategy = AggregateCustomMetricStrategy(min_available_clients=2,fraction_fit=0.5,fraction_evaluate=1.0)
#fl.server.start_server(strategy=strategy)  

#strategy = fl.server.strategy.FedAvg(min_available_clients=2,fraction_fit=0.5,fraction_evaluate=1.0)

fl.server.start_server(config=fl.server.ServerConfig(num_rounds=numRounds),server_address='localhost:'+serverPort,strategy=strategy)