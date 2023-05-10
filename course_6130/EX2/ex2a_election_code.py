def join_agreement_parties(dict_parties_above_threshold, list_of_agreements, knesset):
    """
    Stage 5a - redefine the list of parties according to agreements
    :param dict_parties_above_threshold: a dictionary containing the number of voters (values) for each party (key)
    :param list_of_agreements: a list containing lists. Each list within the list reflects an agreement.
    If two parties has an agreement they appear together in one list.
    If a party does not have any agreement, the list contains only one party name.
    :param knesset: a dictionary with the parties as keys and number of seats as values.
    :return: a dictionary with the agreement parties as keys and number of seats as values.
    """
    agreement_parties = {}
    for agreement in list_of_agreements:
        # init the values for each agreement
        cur_agreement = []
        num_votes_agreement = 0
        num_seats_agreement = 0
        is_one_party_above_threshold = False
        for party in agreement:
            # check if parties pass the threshold (appear in the dict_parties)
            if party in dict_parties_above_threshold.keys():
                cur_agreement.append(party)
                num_votes_agreement += dict_parties_above_threshold[party]
                num_seats_agreement += knesset[party]
                is_one_party_above_threshold = True
        # check if one of the parties in the agreement passed the threshold
        # without this line we will create an empty key for agreement that both parties did not pass
        if is_one_party_above_threshold:
            # the new party name is arbitrary. Can you think of another way to implement this agreement dictionary?
            agreement_parties[":".join(cur_agreement)] = [num_votes_agreement, num_seats_agreement]

    return agreement_parties


def assign_remaining_seats_to_agreements(agreement_parties, num_remaining_seats):
    """
    Stage 5b - divide the rest of the seats
    :param agreement_parties:  a dictionary with the agreement parties as keys and number of seats as values.
    :param num_remaining_seats: number of empty seats from the total number of seats
    :return: an update of the agreement parties dictionary with the additional seats
    """
    agreement_indexes = {}
    # follow the assignment procedure for each empty seat
    for seat_index in range(num_remaining_seats):
        # compute the agreement index - "Moded of the list"
        for party in agreement_parties.keys():
            agreement_indexes[party] = agreement_parties[party][0] / (agreement_parties[party][1] + 1)

        # find the largest index and add one seat
        agreement_parties[max(agreement_indexes, key=agreement_indexes.get)][1] += 1
        # print the agreement parties that gain additional seat
        print("Round %d added %s one more seat" % (seat_index, max(agreement_indexes, key=agreement_indexes.get)))
    return agreement_parties


def agreements_seats_to_parties_seats(agreement_parties_after_addition, dict_parties_above_threshold):
    """
    divide the agreement parties and their seats
    :param agreement_parties_after_addition: an updated dictionary with the agreement parties as
    keys and the updated number of seats as values.
    :param dict_parties_above_threshold: a dictionary containing the number of voters (values) for each party (key)
    :return: a dictionary containing the final results of the election. Parties as keys and number of seats as values.
    """
    final_knesset = {}
    for agreement in agreement_parties_after_addition.keys():
        # if the agreement does not have two parties the agreement seats is the final number of seats of the party
        if ":" not in agreement:
            final_knesset[agreement] = agreement_parties_after_addition[agreement][1]
        # if there are two parties we need to compute the number of seats for each party
        else:
            party1, party2 = agreement.split(":")  # This line match the definition in join_agreement_parties function
            # computes the "Moded pnimi" for a seat
            agreement_seat_index = agreement_parties_after_addition[agreement][0] / \
                                   agreement_parties_after_addition[agreement][1]
            # computes the number of seats according to the "Moded pnimi"
            party1_seats = int(dict_parties_above_threshold[party1] / agreement_seat_index)
            party2_seats = int(dict_parties_above_threshold[party2] / agreement_seat_index)
            # computes the "Moded Reshima" (of the party)
            party1_index = dict_parties_above_threshold[party1] / (party1_seats + 1)
            party2_index = dict_parties_above_threshold[party2] / (party2_seats + 1)
            # the party with the larger "Moded Reshima" gets additional seat
            if party1_index > party2_index:
                final_knesset[party1] = party1_seats + 1
                final_knesset[party2] = party2_seats
            elif party1_index < party2_index:
                final_knesset[party1] = party1_seats
                final_knesset[party2] = party2_seats + 1
            else:
                print("What are the odds???")

    return dict(sorted(final_knesset.items(), key=lambda item: item[1], reverse=True))