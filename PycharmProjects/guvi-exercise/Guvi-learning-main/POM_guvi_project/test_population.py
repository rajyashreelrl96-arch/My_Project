import time
from population_page import PopulationPage

def test_population_counter(setup):

    driver = setup

    url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

    population_page = PopulationPage(driver)

    population_page.open_page(url)
    time.sleep(3)
    print("\nLive Population Counter (Press CTRL + C to stop)\n")

    # population = population_page.get_population()
    # print("Current World Population:", population)

    try:
        while True:
            population = population_page.get_population()
            print("Current World Population:", population)
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nUser stopped the population counter.")