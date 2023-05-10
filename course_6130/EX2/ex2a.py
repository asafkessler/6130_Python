# 315535518, 316539196

import ex2a_election_code as ex2a

def elections_day(dict_parties, list_of_agreements, seats=120, threshold=3.25):
    """
    The function compute the final results - number of seats in the Knesset for each party

    :param dict_parties: a dictionary containing the number of voters (values) for each party (key)
    :param list_of_agreements: a list containing lists. Each list within the list reflects an agreement.
    If two parties has an agreement they appear together in one list.
    If a party does not have any agreement, the list contains only one party name.
    :param seats: number of seats in the Knesset
    :param threshold: percent of votes to enter the Knesset
    :return: a dictionary containing the final number of seats in the Knesset (values) for each party (key)

    """
    # Stage 1 - not included in this algorithm. The results are without the invalid votes

    # Stage 2 - remove parties below the threshold
    print("Stage 2")
    dict_parties_above_threshold = apply_threshold(dict_parties, threshold)

    # Stage 3. votes_per_seat = Hamoded Haklali
    print("Stage 3")
    votes_per_seat = compute_votes_per_seat(dict_parties_above_threshold,seats)
    print("Votes per seat Hamoded Haklali", votes_per_seat)


    # Stage 4 - compute the "wholes" seats according to the votes

    knesset = compute_seats_without_residuals(dict_parties_above_threshold, votes_per_seat)
    num_remaining_seats = seats - sum(knesset.values())
    print("Stage 4")
    print("Number of remaining seats: %d" % num_remaining_seats)

    # Stage 5 - decide who will get the remaining seats
    # Stage 5a - redefine the list of parties according to agreements
    agreement_parties = ex2a.join_agreement_parties(dict_parties_above_threshold, list_of_agreements, knesset)
    print("Stage 5a")
    print(agreement_parties)
    # Stage 5b - divide the rest of the seats
    agreement_parties_after_addition = ex2a.assign_remaining_seats_to_agreements(agreement_parties, num_remaining_seats)
    print("Stage 5b")
    print(agreement_parties_after_addition)

    # Stage 6 - divide the agreement parties and their seats
    final_knesset = ex2a.agreements_seats_to_parties_seats(agreement_parties_after_addition, dict_parties_above_threshold)
    print("Stage 6")
    return final_knesset


def apply_threshold(dict_parties, threshold):
    """
    Stage 2 - remove the parties that do not reach the threshold.

    :param dict_parties: a dictionary containing the number of voters (values) for each party (key)
    :param threshold: percent of votes to enter the Knesset

    :return: dict_parties_above_threshold - dict of the parties without the parties below the threshold
    """
    dict_parties_above_threshold = dict(dict_parties)
    min_votes_needed = sum(list(dict_parties.values())) / 100 * threshold
    temp_list = []
    for key, val in dict_parties_above_threshold.items():
        if dict_parties_above_threshold[key] <= min_votes_needed:
            temp_list.append(key)
        else:
            continue
    for key in temp_list:
        del dict_parties_above_threshold[key]

    return dict_parties_above_threshold



def compute_votes_per_seat(dict_parties_above_threshold, seats):
    """
    Stage 3 - compute the votes_per_seat = Hamoded Haklali
    :param dict_parties_above_threshold:
    :param seats: number of seats in the Knesset
    :return: votes_per_seat - number of votes per seat after removing the parties that did not reach the threshold
    """
    votes_per_seat = int(sum(list(dict_parties_above_threshold.values())) / seats)
    return votes_per_seat


def compute_seats_without_residuals(dict_parties_above_threshold, votes_per_seat):
    """
    Stage 4 - compute the "wholes" seats according to the votes

    :param dict_parties_above_threshold: a dictionary containing the number of voters (values) for each party (key)
    :param votes_per_seat: Hamoded Haklali - how many votes equal a seat
    :return: knesset - a dictionary with the parties as keys and number of seats as values.
    The number of seats are round down (3.9 -> 3)
    """
    for key, val in dict_parties_above_threshold.items():
        seats_num = int(val / votes_per_seat)
        dict_parties_above_threshold.update({key:seats_num})
    print(dict_parties_above_threshold.values())
    return dict_parties_above_threshold



if __name__ == "__main__":
    dict_parties = {"Likud": 1115336, "Yesh-Atid": 847435, "Shas": 392964, "Hamachane-Hamamlachti": 432482,
                    "Tzionut-Datit": 516470, "Yahadot-Hatora": 280194, "Israel-Beitanu": 213687, 
					"Harshima-Haaravit": 194047, "Hareshima-Hameshutefet": 178735, "Haavoda": 175992, 
                    "Meretz": 150793, "Balad": 138617, "Habit-Hayehudi": 56775}
    list_of_agreements = [["Likud", "Tzionut-Datit"], ["Yesh-Atid", "Hamachane-Hamamlachti"],
                          ["Shas", "Yahadot-Hatora"], ["Haavoda", "Meretz"]]
    final_knesset = elections_day(dict_parties, list_of_agreements)
    # print the results
    print(final_knesset)
    # print the total amount of seats - should be 120
    print(sum(final_knesset.values()))
