def default_step(init_val=3, step_every=1, p=-1):
    def fraction_function(n):
        return init_val * ((n // step_every) + 1) ** p
    return fraction_function
