if event.key == K_LEFT and perso_x >= 0 and perso_x <= 1680:
                        perso_x = perso_x - 40
                    else:
                        perso_x = perso_x
                    if event.key == K_RIGHT and perso_x >= 0 and perso_x <= 1680:
                        perso_x = perso_x + 40
                    else:
                        perso_x = perso_x
                    if event.key == K_UP and perso_y >= 0 and perso_y <= 1000:
                        perso_y = perso_y - 40
                    else:
                        perso_y = perso_y
                    if event.key == K_DOWN and perso_y >= 0 and perso_y <= 1000:
                        perso_y = perso_y + 40
                    else:
                        perso_y = perso_y
