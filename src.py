def build_model(nodes, learn_rate):

    my_layers = []
    # Add input layer
    my_layers.append(layers.Dense(nodes[0], activation='swish', input_shape=[len(train_features.keys())]))
    # Add hidden layers
    for layer_nodes in nodes[1:]:
        my_layers.append(layers.Dense(layer_nodes, activation=tf.keras.layers.LeakyReLU(alpha=0.1)))
    # Add output layer
    my_layers.append(layers.Dense(1))  

    # Define network and optimizer
    model = keras.Sequential(my_layers)
    optimizer = keras.optimizers.Adam(learn_rate)
    # Build model with 
    model.compile(
        loss = 'mape',
        optimizer=optimizer,
        metrics=['mae', 'mse', 'msle', 'mape','accuracy'])
      
     
    
    model_name = 'snv_cross_entropy_nodes-' + '-'.join(map(str, nodes)) + '_rate-' + str(learn_rate)
    return model_name, model
