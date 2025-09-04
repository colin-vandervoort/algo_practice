import cx from 'classnames';
// import { Component } from 'react';
import react, { useState } from 'react';

function LikeButton(props) {
    const [likesState, setLikesState] = useState({
        like_count_others: 100,
        current_user_has_liked: false,
    })
    let like_count = likesState.like_count_others
    if (likesState.current_user_has_liked) {
        like_count += 1
    }

    return (
        <>
            <div>
                <h2>Like Button</h2>
            </div>
            <button
                onClick={() => setLikesState({
                    ...likesState,
                    current_user_has_liked: !likesState.current_user_has_liked,
                })}
                className={cx({"like-button": true, "liked": likesState.current_user_has_liked })}
            >
                {"Like | "}
                <span className="likes-counter">{like_count}</span>
            </button>
            <style>{`
                .like-button {
                    font-size: 1rem;
                    padding: 5px 10px;
                    color:  #585858;
                }
                .liked {
                    font-weight: bold;
                    color: #1565c0;
                }
            `}</style>
        </>
    )
}

export default LikeButton
