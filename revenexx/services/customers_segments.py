from ..service import Service
from typing import Any, Dict, List, Optional, Union
from ..exception import RevenexxException
from ..utils.deprecated import deprecated
from ..enums.source import Source;
from ..enums.segment_member_source import SegmentMemberSource;
from ..models.error import Error;
from ..enums.rule_match import RuleMatch;
from ..enums.segment_rule_match import SegmentRuleMatch;
from ..models.segment_rule_condition import SegmentRuleCondition;
from ..enums.target import Target;

class CustomersSegments(Service):

    def __init__(self, client) -> None:
        super(CustomersSegments, self).__init__(client)

    def customers_segment_members_list(
        self,
        id: Optional[str] = None,
        segment_id: Optional[str] = None,
        organization_id: Optional[str] = None,
        source: Optional[Source] = None,
        created_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        One organization inside one segment, plus the record of how it got there: `source: "manual"` for a company somebody put in, `source: "rule"` for one the rule engine matched. That distinction is what lets a recompute rewrite its own rows and leave every hand-picked one alone. The membership rows themselves — the answer to "which companies are in this segment" (`segment_id`) and to "which segments is this company in" (`organization_id`). Paged with `limit`/`offset`/`order`.

        Parameters
        ----------
        id : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the membership row.
        segment_id : Optional[str]
            Filter to one segment — its members.
        organization_id : Optional[str]
            Filter to one company — the segments it belongs to. The same route answers both questions.
        source : Optional[Source]
            Filter by how the membership came about. `manual` is the hand-picked set a recompute will never touch.
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the organization joined the segment.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segment_members'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if segment_id is not None:
            api_params['segment_id'] = self._normalize_value(segment_id)
        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if source is not None:
            api_params['source'] = self._normalize_value(source)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_segment_members_create(
        self,
        organization_id: str,
        segment_id: str,
        source: Optional[SegmentMemberSource] = None
    ) -> Error:
        """
        One organization inside one segment, plus the record of how it got there: `source: "manual"` for a company somebody put in, `source: "rule"` for one the rule engine matched. That distinction is what lets a recompute rewrite its own rows and leave every hand-picked one alone. Adds a company to a segment BY HAND. The row is `source: "manual"`, which is what protects it: a rule recompute rewrites the rule-derived rows of that segment and never touches this one. A create cannot omit `segment_id` and `organization_id`; everything else is optional or defaulted by the database. Two rows of this tenant may not share the combination of `segment_id` + `organization_id`.

        Parameters
        ----------
        organization_id : str
            The member company. Segments group companies, never people — a person is reached through their organization.
        segment_id : str
            The segment.
        source : Optional[SegmentMemberSource]
            How this membership came about: 'manual' is hand-picked, 'rule' was materialized by a recompute. The distinction is load-bearing — a recompute only ever inserts and deletes 'rule' rows, so a hand-picked member survives every rule change. Default 'manual'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segment_members'
        api_params = {}
        if organization_id is None:
            raise RevenexxException('Missing required parameter: "organization_id"')

        if segment_id is None:
            raise RevenexxException('Missing required parameter: "segment_id"')


        api_params['organization_id'] = self._normalize_value(organization_id)
        api_params['segment_id'] = self._normalize_value(segment_id)
        if source is not None:
            api_params['source'] = self._normalize_value(source)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segment_members_delete(
        self,
        id: str
    ) -> Error:
        """
        One organization inside one segment, plus the record of how it got there: `source: "manual"` for a company somebody put in, `source: "rule"` for one the rule engine matched. That distinction is what lets a recompute rewrite its own rows and leave every hand-picked one alone. Takes the company out of the segment. If the segment carries rules and the company still matches them, the next recompute puts it back; remove it from the rule, not from the list. Nothing else in this app points at it, so nothing else goes with it.

        Parameters
        ----------
        id : str
            The segment membership to delete.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segment_members/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segment_members_get(
        self,
        id: str
    ) -> Error:
        """
        One organization inside one segment, plus the record of how it got there: `source: "manual"` for a company somebody put in, `source: "rule"` for one the rule engine matched. That distinction is what lets a recompute rewrite its own rows and leave every hand-picked one alone. One membership row by id, with the `source` that says how it came about.

        Parameters
        ----------
        id : str
            The segment membership to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segment_members/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segment_members_update(
        self,
        id: str,
        organization_id: Optional[str] = None,
        segment_id: Optional[str] = None,
        source: Optional[SegmentMemberSource] = None
    ) -> Error:
        """
        One organization inside one segment, plus the record of how it got there: `source: "manual"` for a company somebody put in, `source: "rule"` for one the rule engine matched. That distinction is what lets a recompute rewrite its own rows and leave every hand-picked one alone. A partial update. In practice there is little to change — a membership is a pair of ids — so this exists for the `source` correction rather than as the normal path. Two rows of this tenant may not share the combination of `segment_id` + `organization_id`.

        Parameters
        ----------
        id : str
            The segment membership to update.
        organization_id : Optional[str]
            The member company. Segments group companies, never people — a person is reached through their organization.
        segment_id : Optional[str]
            The segment.
        source : Optional[SegmentMemberSource]
            How this membership came about: 'manual' is hand-picked, 'rule' was materialized by a recompute. The distinction is load-bearing — a recompute only ever inserts and deletes 'rule' rows, so a hand-picked member survives every rule change. Default 'manual'.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segment_members/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if organization_id is not None:
            api_params['organization_id'] = self._normalize_value(organization_id)
        if segment_id is not None:
            api_params['segment_id'] = self._normalize_value(segment_id)
        if source is not None:
            api_params['source'] = self._normalize_value(source)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_list(
        self,
        id: Optional[str] = None,
        code: Optional[str] = None,
        position: Optional[float] = None,
        rule_match: Optional[RuleMatch] = None,
        rules_computed_at: Optional[str] = None,
        created_at: Optional[str] = None,
        updated_at: Optional[str] = None,
        limit: Optional[float] = None,
        offset: Optional[float] = None,
        order: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        A segment is a named group of ORGANIZATIONS — never of people — built by hand, by rule, or both at once. It is what a price list, a campaign or a shipping option is pointed at when the answer is "these customers, not those". Every segment this tenant keeps, with its stored rules. Any column filters and the page is `limit`/`offset`/`order`. Which companies are actually IN one is `segment_members`, because the rule half is materialized rather than evaluated on read.

        Parameters
        ----------
        id : Optional[str]
            Filter to rows whose `id` is exactly this value. Primary key of the segment.
        code : Optional[str]
            Filter by exact segment code.
        position : Optional[float]
            Filter to rows whose `position` is exactly this value. Sort order in the cockpit, ascending. Ties fall back to insertion order.
        rule_match : Optional[RuleMatch]
            Filter to rows whose `rule_match` is exactly this value. How the conditions combine: 'all' (default) is AND, 'any' is OR. Null means the same as 'all'.
        rules_computed_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the rule last finished a COMPLETE recompute. Null after a rule change, and while a chunked recompute is still running — so it doubles as "are the rule memberships trustworthy right now?".
        created_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When the segment was created.
        updated_at : Optional[str]
            Exact timestamp equality — this API has no range filter. To bound a period, sort with `order` and page. When any column of this row last changed.
        limit : Optional[float]
            Page size (default 50, max 200).
        offset : Optional[float]
            Row offset for pagination (default 0).
        order : Optional[str]
            Sort by one column: 'column' | 'column.asc' | 'column.desc'. A bare column sorts ascending. Anything else is refused with 400.
        
        Returns
        -------
        Dict[str, Any]
            API response as a dictionary
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments'
        api_params = {}

        if id is not None:
            api_params['id'] = self._normalize_value(id)
        if code is not None:
            api_params['code'] = self._normalize_value(code)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        if rule_match is not None:
            api_params['rule_match'] = self._normalize_value(rule_match)
        if rules_computed_at is not None:
            api_params['rules_computed_at'] = self._normalize_value(rules_computed_at)
        if created_at is not None:
            api_params['created_at'] = self._normalize_value(created_at)
        if updated_at is not None:
            api_params['updated_at'] = self._normalize_value(updated_at)
        if limit is not None:
            api_params['limit'] = self._normalize_value(limit)
        if offset is not None:
            api_params['offset'] = self._normalize_value(offset)
        if order is not None:
            api_params['order'] = self._normalize_value(order)

        response = self.client.call('get', api_path, {
        }, api_params)

        return response


    def customers_segments_create(
        self,
        code: str,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        rule_match: Optional[SegmentRuleMatch] = None,
        rules: Optional[Dict[str, Any]] = None
    ) -> Error:
        """
        A segment is a named group of ORGANIZATIONS — never of people — built by hand, by rule, or both at once. It is what a price list, a campaign or a shipping option is pointed at when the answer is "these customers, not those". Creates the group. Rules are optional: leave them out for a hand-picked list, or store a rule document and let the recompute keep the membership up to date. The `code` is what other apps point at, so pick it deliberately. `code` is the only field a create cannot omit; everything else is optional or defaulted by the database. Two rows of this tenant may not share `code`.

        Parameters
        ----------
        code : str
            Stable identifier, unique per tenant — what other apps and integrations name the segment by. Free text, but lowercase with underscores is the convention every seeded vocabulary follows.
        labels : Optional[Dict[str, Any]]
            Localized display names keyed by language tag. Null means nobody translated it and a client falls back to showing the code.
        position : Optional[float]
            Sort order in the cockpit, ascending. Ties fall back to insertion order. Default 0.
        rule_match : Optional[SegmentRuleMatch]
            How the conditions combine: 'all' (default) is AND, 'any' is OR. Null means the same as 'all'.
        rules : Optional[Dict[str, Any]]
            The selector that decides membership, stored verbatim. Null means the segment is manual-only. The same rule language product categories use, evaluated over organization columns, `setting:<key>` entries and the organization_metrics projection — so 'no order in 365 days' is expressible without joining the orders app. Null makes the segment manual-only. Changing it does not move a single membership — run the recompute.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments'
        api_params = {}
        if code is None:
            raise RevenexxException('Missing required parameter: "code"')


        api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['rule_match'] = self._normalize_value(rule_match)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_rules_recompute_all(
        self,
        data: Dict[str, Any]
    ) -> Error:
        """
        Same sync as the single-segment recompute, applied to every segment with non-null rules. A failing segment is reported in its result entry instead of aborting the run. The run shares one budget: a segment that does not fit reports done:false (or skipped:true) and keeps rules_computed_at null, so the next call resumes it from its own data. Repeat until the top-level done is true.

        Parameters
        ----------
        data : Dict[str, Any]
            Request body
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments/rules/recompute-all'
        api_params = {}
        if data is None:
            raise RevenexxException('Missing required parameter: "data"')


        api_params['data'] = self._normalize_value(data)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_delete(
        self,
        id: str
    ) -> Error:
        """
        A segment is a named group of ORGANIZATIONS — never of people — built by hand, by rule, or both at once. It is what a price list, a campaign or a shipping option is pointed at when the answer is "these customers, not those". Removes the segment. Anything in another app that points at its `code` — a price list, a campaign — is left pointing at nothing, because no app may hold a foreign key into another (ADR-0055). Deleting one takes every `segment_members` row that points at it with it — the foreign keys decide, not this route.

        Parameters
        ----------
        id : str
            The segment to delete.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('delete', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_get(
        self,
        id: str
    ) -> Error:
        """
        A segment is a named group of ORGANIZATIONS — never of people — built by hand, by rule, or both at once. It is what a price list, a campaign or a shipping option is pointed at when the answer is "these customers, not those". One segment by id, including the rule document it carries. A segment with no rules is hand-picked and completely valid.

        Parameters
        ----------
        id : str
            The segment to read.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))


        response = self.client.call('get', api_path, {
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_update(
        self,
        id: str,
        code: Optional[str] = None,
        labels: Optional[Dict[str, Any]] = None,
        position: Optional[float] = None,
        rule_match: Optional[SegmentRuleMatch] = None,
        rules: Optional[Dict[str, Any]] = None
    ) -> Error:
        """
        A segment is a named group of ORGANIZATIONS — never of people — built by hand, by rule, or both at once. It is what a price list, a campaign or a shipping option is pointed at when the answer is "these customers, not those". A partial update — send only what changes. Editing the rules does NOT re-evaluate them: that is `POST /customers/segments/{segment_id}/rules/recompute`, so a half-typed rule never silently empties a live segment. Two rows of this tenant may not share `code`.

        Parameters
        ----------
        id : str
            The segment to update.
        code : Optional[str]
            Stable identifier, unique per tenant — what other apps and integrations name the segment by. Free text, but lowercase with underscores is the convention every seeded vocabulary follows.
        labels : Optional[Dict[str, Any]]
            Localized display names keyed by language tag. Null means nobody translated it and a client falls back to showing the code.
        position : Optional[float]
            Sort order in the cockpit, ascending. Ties fall back to insertion order. Default 0.
        rule_match : Optional[SegmentRuleMatch]
            How the conditions combine: 'all' (default) is AND, 'any' is OR. Null means the same as 'all'.
        rules : Optional[Dict[str, Any]]
            The selector that decides membership, stored verbatim. Null means the segment is manual-only. The same rule language product categories use, evaluated over organization columns, `setting:<key>` entries and the organization_metrics projection — so 'no order in 365 days' is expressible without joining the orders app. Null makes the segment manual-only. Changing it does not move a single membership — run the recompute.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments/{id}'
        api_params = {}
        if id is None:
            raise RevenexxException('Missing required parameter: "id"')

        api_path = api_path.replace('{id}', str(self._normalize_value(id)))

        if code is not None:
            api_params['code'] = self._normalize_value(code)
        api_params['labels'] = self._normalize_value(labels)
        if position is not None:
            api_params['position'] = self._normalize_value(position)
        api_params['rule_match'] = self._normalize_value(rule_match)
        if rules is not None:
            api_params['rules'] = self._normalize_value(rules)

        response = self.client.call('put', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_rules_preview(
        self,
        segment_id: str,
        conditions: List[SegmentRuleCondition],
        rule_match: Optional[RuleMatch] = None,
        target: Optional[Target] = None
    ) -> Error:
        """
        A dry run: it answers how many organizations the rule would select, with a handful of them by name, and writes nothing at all. Evaluates the rule document in the REQUEST BODY (not the stored segments.rules), so the cockpit can preview an unsaved rule. Costs a single count query for the common single-query rule; 'any' rules and rules repeating a column are combined in the app and capped at 5000 ids, in which case 'capped' is true and 'count' is a LOWER bound. Membership is never touched.

        Parameters
        ----------
        segment_id : str
            The segment the preview is filed under. Its stored rules are NOT read — the rule comes from the body — but it has to exist.
        conditions : List[SegmentRuleCondition]
            The conditions, combined by `rule_match`. At least one, at most 25.
        rule_match : Optional[RuleMatch]
            How the conditions combine. Default 'all'.
        target : Optional[Target]
            Only 'organizations' is supported; any other value is rejected. A segment groups COMPANIES — the people are reached through them.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments/{segment_id}/rules/preview'
        api_params = {}
        if segment_id is None:
            raise RevenexxException('Missing required parameter: "segment_id"')

        if conditions is None:
            raise RevenexxException('Missing required parameter: "conditions"')

        api_path = api_path.replace('{segment_id}', str(self._normalize_value(segment_id)))

        api_params['conditions'] = self._normalize_value(conditions)
        api_params['rule_match'] = self._normalize_value(rule_match)
        api_params['target'] = self._normalize_value(target)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)


    def customers_segments_rules_recompute(
        self,
        segment_id: str,
        cursor: Optional[str] = None
    ) -> Error:
        """
        Evaluates segments.rules (NOT the request body), then inserts the newly matching organizations as source='rule' rows and deletes the rule rows that no longer match. Manual (source='manual') memberships are never inserted, deleted or shadowed. Bounded by a wall-clock budget below the gateway's upstream timeout: when 'done' is false, POST again with the returned 'cursor' until it is true. added/removed/processed count THIS call only. Omitting 'cursor' resumes an unfinished pass and starts a fresh one after a completed pass; an explicit null always restarts. segments.rules_computed_at is stamped only when the pass completes.

        Parameters
        ----------
        segment_id : str
            The segment whose stored rules are evaluated.
        cursor : Optional[str]
            Continuation token from a previous response — the id of the last organization the pass touched. Omit to resume or start automatically; pass null to force a restart from the beginning.
        
        Returns
        -------
        Error
            API response as a typed Pydantic model
        
        Raises
        ------
        RevenexxException
            If API request fails
        """

        api_path = '/v1/customers/segments/{segment_id}/rules/recompute'
        api_params = {}
        if segment_id is None:
            raise RevenexxException('Missing required parameter: "segment_id"')

        api_path = api_path.replace('{segment_id}', str(self._normalize_value(segment_id)))

        api_params['cursor'] = self._normalize_value(cursor)

        response = self.client.call('post', api_path, {
            'content-type': 'application/json',
        }, api_params)

        return self._parse_response(response, model=Error)

