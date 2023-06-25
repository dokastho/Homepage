import PropTypes from 'prop-types';
import React from 'react'
import Group from './Group';

class Topic extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      name: "",
      groups: {}
    }
  }

  componentDidMount() {
    const { name, groups } = this.props.content;
    this.setState({ name, groups });
  }

  render() {
    const {
      setTopicFocus,
      topicIdx,
      maxTopicIdx,
    } = this.props;

    const { name, groups } = this.state;

    // sort groups by groupOrder
    const groupKeys = Object.keys(groups).map((groupId) => {
      return ({ groupId: groupId, groupOrder: groups[groupId].groupOrder });
    })
    const sortedGroups = groupKeys.sort((a, b) => a.groupOrder - b.groupOrder);


    return (
      <div className='topic' key={topicIdx}>
        <h1>{name}</h1>
        {
          sortedGroups.map((group, i) => {
            return (<Group content={groups[group.groupId]} />);
          })
        }
        {
          topicIdx === 0 ? null : (
            <button onClick={() => { setTopicFocus(topicIdx - 1) }}>&lt;-</button>
          )
        }
        {
          topicIdx === maxTopicIdx ? null : (
            <button onClick={() => { setTopicFocus(topicIdx + 1) }}>-&gt;</button>
          )
        }
      </div>
    );
  }
}

Topic.propTypes = {
  // prop types go here
  content: PropTypes.object,
  topicIdx: PropTypes.number.isRequired,
  maxTopicIdx: PropTypes.number.isRequired,
  // methods:
  // setTopicFocus
};

Topic.defaultProps = {
  // default prop values go here if not required
};

export default Topic

