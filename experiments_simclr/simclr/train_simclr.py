for x_i, x_j in train_loader:
    h_i = encoder(x_i)
    h_j = encoder(x_j)
    z_i = projection_head(h_i)
    z_j = projection_head(h_j)
    
    loss = nt_xent_loss(z_i, z_j)
    loss.backward()
    optimizer.step()
