import PropTypes from 'prop-types';
import React from 'react'

class Picker extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    const {
      topics,
      setTopicFocus,
    } = this.props;
    return (
      <div className='picker'>
        {
          topics.map((topic) => {
            const { idx, name } = topic;
            return <button id={idx} key={idx} onClick={() => { setTopicFocus(idx) }}>{name}</button>
          })
        }
      </div>
    );
  }
}

Picker.propTypes = {
  topics: PropTypes.instanceOf(Array).isRequired  // array of pairs: name and topicId

  // methods
  // setTopicFocus
};

Picker.defaultProps = {
  // default prop values go here if not required
};

export default Picker
