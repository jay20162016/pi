import copy 

def scramble( nums, prefix ):
    if len( nums ) == 1:
        prefix.append( nums[ 0 ] )
        print '%s\n' % prefix 
        return
    for n in nums:
        new_nums = copy.deepcopy( nums )
        new_nums.remove( n )
        new_prefix = copy.deepcopy( prefix )
        new_prefix.append( n )
        scramble( new_nums, new_prefix )
        

scramble( range(1,4), [] )